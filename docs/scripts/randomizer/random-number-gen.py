import random
import sys
import csv
import logging
from datetime import datetime
import argparse
try:
    import tkinter as tk
    from tkinter import messagebox, filedialog
except ImportError:
    tk = None  # GUI will not be available if Tkinter is not installed

# Configure Logging
logging.basicConfig(
    filename='number_selector.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_user_input(prompt, default):
    """
    Helper function to get user input with a default value.
    """
    user_input = input(f"{prompt} [{default}]: ")
    return user_input.strip() or default

def validate_positive_integer(value, name):
    """
    Validates that the provided value is a positive integer.
    """
    try:
        ivalue = int(value)
        if ivalue <= 0:
            raise ValueError
        return ivalue
    except ValueError:
        print(f"Error: {name} must be a positive integer.")
        logging.error(f"Invalid input for {name}: {value}")
        sys.exit(1)

def select_numbers(available_numbers, num_selections, method='sample'):
    """
    Select numbers using the specified randomization method.
    """
    logging.debug(f"Selecting {num_selections} numbers using method: {method}")
    if method == 'sample':
        return random.sample(available_numbers, num_selections)
    elif method == 'shuffle':
        shuffled = available_numbers.copy()
        random.shuffle(shuffled)
        return shuffled[:num_selections]
    elif method == 'choices':
        return random.choices(available_numbers, k=num_selections)
    else:
        logging.error(f"Unknown randomization method: {method}")
        raise ValueError("Unknown randomization method.")

def export_results(sets, filename, file_format='csv'):
    """
    Export the generated sets to a file in the specified format.
    """
    logging.debug(f"Exporting results to {filename} in {file_format} format.")
    try:
        if file_format == 'csv':
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Set Number', 'Selected Numbers'])
                for i, s in enumerate(sets, 1):
                    writer.writerow([i, ', '.join(map(str, s))])
        elif file_format == 'txt':
            with open(filename, 'w') as txtfile:
                for i, s in enumerate(sets, 1):
                    txtfile.write(f"Set {i}: {s}\n")
        else:
            logging.error(f"Unsupported file format: {file_format}")
            print("Unsupported file format. Please choose 'csv' or 'txt'.")
            return
        print(f"Results successfully exported to {filename}")
        logging.info(f"Results exported to {filename}")
    except Exception as e:
        logging.error(f"Failed to export results: {e}")
        print(f"Failed to export results: {e}")

def main():
    print("### Comprehensive Number Selector ###\n")
    
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Select random numbers with enhanced features.")
    parser.add_argument('--gui', action='store_true', help='Launch the GUI mode.')
    args = parser.parse_args()
    
    if args.gui:
        if tk is None:
            print("Tkinter is not available. GUI mode cannot be launched.")
            sys.exit(1)
        launch_gui()
    else:
        # CLI Mode
        try:
            # Get and validate range of numbers
            start_range = validate_positive_integer(get_user_input("Enter the start of the range", "1"), "Start of range")
            end_range = validate_positive_integer(get_user_input("Enter the end of the range", "15"), "End of range")
            
            if end_range < start_range:
                print("Error: End of range must be greater than or equal to start of range.")
                logging.error("End of range is less than start of range.")
                sys.exit(1)
            
            available_numbers = list(range(start_range, end_range + 1))
            total_available = len(available_numbers)
            logging.info(f"Available numbers: {available_numbers}")
            
            # Get and validate number of selections
            num_selections = validate_positive_integer(get_user_input("How many numbers to select", "6"), "Number of selections")
            
            if num_selections > total_available and method != 'choices':
                print(f"Error: Cannot select {num_selections} numbers from a range of {total_available} numbers.")
                logging.error("Number of selections exceeds available numbers.")
                sys.exit(1)
            
            # Get number of sets to generate
            num_sets = validate_positive_integer(get_user_input("How many sets to generate", "1"), "Number of sets")
            
            # Choose randomization method
            print("\nSelect Randomization Method:")
            print("1. Random Sample (No Replacement)")
            print("2. Shuffle and Select")
            print("3. Random Choices (With Replacement)")
            method_choice = get_user_input("Enter choice (1/2/3)", "1")
            methods = {'1': 'sample', '2': 'shuffle', '3': 'choices'}
            method = methods.get(method_choice, 'sample')
            if method not in methods.values():
                print("Invalid method selected. Defaulting to 'sample'.")
                method = 'sample'
            logging.info(f"Randomization method selected: {method}")
            
            # Optionally set a seed for reproducibility
            seed_input = get_user_input("Enter a seed for randomness (or leave blank for random)", "")
            if seed_input:
                try:
                    seed = int(seed_input)
                    random.seed(seed)
                    print(f"Random seed set to: {seed}\n")
                    logging.info(f"Random seed set to: {seed}")
                except ValueError:
                    print("Invalid seed input. Proceeding without setting seed.\n")
                    logging.warning("Invalid seed input provided.")
            
            # Generate and collect the selected numbers
            all_selected_sets = []
            for set_num in range(1, num_sets + 1):
                selected_numbers = select_numbers(available_numbers, num_selections, method)
                all_selected_sets.append(selected_numbers)
                print(f"Set {set_num}: {selected_numbers}")
                logging.info(f"Set {set_num}: {selected_numbers}")
            
            # Exporting results
            export_choice = get_user_input("Would you like to export the results? (y/n)", "n").lower()
            if export_choice == 'y':
                file_format = get_user_input("Enter file format ('csv' or 'txt')", "csv").lower()
                default_filename = f"number_sets_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{file_format}"
                filename = get_user_input("Enter filename", default_filename)
                export_results(all_selected_sets, filename, file_format)
            
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            logging.warning("Operation cancelled by user.")
            sys.exit(0)

def launch_gui():
    """
    Launches the GUI using Tkinter.
    """
    def generate_sets():
        try:
            start = int(start_entry.get())
            end = int(end_entry.get())
            if end < start:
                messagebox.showerror("Input Error", "End of range must be >= start of range.")
                logging.error("GUI: End of range less than start.")
                return
            available = list(range(start, end + 1))
            num_sel = int(num_select_entry.get())
            num_sets_val = int(num_sets_entry.get())
            method_val = method_var.get()
            
            if num_sel > len(available) and method_val != 'choices':
                messagebox.showerror("Input Error", f"Cannot select {num_sel} numbers from {len(available)} available.")
                logging.error("GUI: Number of selections exceeds available numbers.")
                return
            
            seed_val = seed_entry.get()
            if seed_val:
                try:
                    seed = int(seed_val)
                    random.seed(seed)
                    logging.info(f"GUI: Random seed set to {seed}")
                except ValueError:
                    messagebox.showwarning("Input Warning", "Invalid seed input. Proceeding without setting seed.")
                    logging.warning("GUI: Invalid seed input.")
            
            all_sets = []
            output_text.delete(1.0, tk.END)
            for i in range(1, num_sets_val + 1):
                selected = select_numbers(available, num_sel, method_val)
                all_sets.append(selected)
                output_text.insert(tk.END, f"Set {i}: {selected}\n")
                logging.info(f"GUI Set {i}: {selected}")
            
            # Export option
            if export_var.get():
                file_format = file_format_var.get()
                default_filename = f"number_sets_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{file_format}"
                filename = filedialog.asksaveasfilename(
                    defaultextension=f".{file_format}",
                    filetypes=[(f"{file_format.upper()} files", f"*.{file_format}"), ("All files", "*.*")]
                )
                if filename:
                    export_results(all_sets, filename, file_format)
        except ValueError as ve:
            messagebox.showerror("Input Error", "Please enter valid integer values.")
            logging.error(f"GUI: Invalid input - {ve}")

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    root = tk.Tk()
    root.title("Comprehensive Number Selector")
    root.geometry("500x600")
    
    # Input Frame
    input_frame = tk.Frame(root)
    input_frame.pack(pady=10)

    tk.Label(input_frame, text="Start of Range:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
    start_entry = tk.Entry(input_frame)
    start_entry.insert(0, "1")
    start_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(input_frame, text="End of Range:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
    end_entry = tk.Entry(input_frame)
    end_entry.insert(0, "15")
    end_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(input_frame, text="Numbers to Select:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
    num_select_entry = tk.Entry(input_frame)
    num_select_entry.insert(0, "6")
    num_select_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(input_frame, text="Number of Sets:").grid(row=3, column=0, padx=5, pady=5, sticky='e')
    num_sets_entry = tk.Entry(input_frame)
    num_sets_entry.insert(0, "1")
    num_sets_entry.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(input_frame, text="Random Seed:").grid(row=4, column=0, padx=5, pady=5, sticky='e')
    seed_entry = tk.Entry(input_frame)
    seed_entry.grid(row=4, column=1, padx=5, pady=5)

    # Randomization Method
    method_var = tk.StringVar(value='sample')
    methods_frame = tk.LabelFrame(root, text="Randomization Method")
    methods_frame.pack(pady=10)

    tk.Radiobutton(methods_frame, text="Random Sample (No Replacement)", variable=method_var, value='sample').pack(anchor='w')
    tk.Radiobutton(methods_frame, text="Shuffle and Select", variable=method_var, value='shuffle').pack(anchor='w')
    tk.Radiobutton(methods_frame, text="Random Choices (With Replacement)", variable=method_var, value='choices').pack(anchor='w')

    # Export Options
    export_var = tk.BooleanVar()
    export_check = tk.Checkbutton(root, text="Export Results", variable=export_var)
    export_check.pack(pady=5)

    file_format_var = tk.StringVar(value='csv')
    file_format_frame = tk.Frame(root)
    file_format_frame.pack()
    tk.Radiobutton(file_format_frame, text="CSV", variable=file_format_var, value='csv').pack(side='left', padx=5)
    tk.Radiobutton(file_format_frame, text="TXT", variable=file_format_var, value='txt').pack(side='left', padx=5)

    # Generate Button
    generate_button = tk.Button(root, text="Generate", command=generate_sets)
    generate_button.pack(pady=10)

    # Output Text
    output_frame = tk.Frame(root)
    output_frame.pack(pady=10, fill='both', expand=True)
    output_text = tk.Text(output_frame, height=15)
    output_text.pack(fill='both', expand=True)

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()
