async function testAPI() {
  console.log('Testing Literary Vault API...');

  try {
    // Test categories
    const categories = await window.literaryVaultAPI.get_categories();
    console.log('Categories loaded:', categories);
    
    // Test random question
    const randomQuestion = await window.literaryVaultAPI.get_random_question();
    console.log('Random question:', randomQuestion);
    
    // Test category questions
    for (const category of categories) {
      const questions = await window.literaryVaultAPI.get_category_questions({ category });
      console.log(`${category} questions:`, questions.length);
      
      const stats = await window.literaryVaultAPI.get_category_stats({ category });
      console.log(`${category} stats:`, stats);
    }
    
    console.log('All tests passed!');
    
  } catch (error) {
    console.error('Test failed:', error);
  }
} 