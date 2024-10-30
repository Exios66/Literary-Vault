---
icon: git
---

# Asking GitHub Copilot questions in GitHub

You can use GitHub Copilot Chat in GitHub to answer general questions about software development, or specific questions about the issues or code in a repository.

Note

GitHub Copilot Chat in GitHub is currently in public preview and is subject to change.

### [Overview](broken-reference) <a href="#overview" id="overview"></a>

GitHub Copilot Chat in GitHub is a chat interface that lets you ask and receive answers to coding-related questions on the GitHub website.

Copilot Chat can help you with a variety of coding-related tasks, like offering you code suggestions, providing natural language descriptions of a piece of code's functionality and purpose, generating unit tests for your code, and proposing fixes for bugs in your code. For more information, see "Responsible use of GitHub Copilot Chat in GitHub."

On GitHub, you can use Copilot Chat to ask:

* General software-related questions, without a particular context. For more information, see "[Asking a general question about software development](broken-reference)."
* Exploratory questions asked in the context of a specific repository. For more information, see "[Asking exploratory questions about a repository](broken-reference)."
* Questions asked in the context of a specific repository, file or symbol. For more information, see "[Asking a question about a specific file or symbol](broken-reference)."
* Questions about a specific file or specified lines of code within a file. For more information, see "[Asking questions about specific pieces of code](broken-reference)."
* Questions about a pull request diff. For more information, see "[Finding out about the changes in a pull request](broken-reference)."
* Questions about a specific issue. For more information, see "[Asking a question about a specific issue or discussion](broken-reference)."

#### [Limitations](broken-reference) <a href="#limitations" id="limitations"></a>

* Chat responses may be suboptimal if you ask questions about a specific repository that you've selected as a context, and the repository has not been indexed for semantic code search. Anyone with a subscription to GitHub Copilot who has write access to a repository can index that repository. For more information, see "Indexing repositories for Copilot Chat."
* The quality of the results from Copilot Chat may, in some situations, be degraded if very large files, or a large number of files, are used as a context for a question.

### [Powered by skills](broken-reference) <a href="#powered-by-skills" id="powered-by-skills"></a>

Copilot is powered by a collection of skills that are dynamically selected based on the question you ask. You can tell which skill Copilot used by clicking  to expand the status information in the chat window.

You can explicitly ask GitHub Copilot Chat in GitHub to use a particular skill - for example, `Use the Bing skill to find the latest GPT4 model from OpenAI`.

#### [Currently available skills](broken-reference) <a href="#currently-available-skills" id="currently-available-skills"></a>

You can generate a list of currently available skills by asking Copilot: `What skills are available?`

The skills you can use in Copilot Chat in GitHub include those shown in the table below.

| Skill                        | Description                                                                                                                                                                                                                                                                                                                                                                                         | Enabled by default?                                                                                                                                                             | Example question                                                                                                           |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Commit details**           | Retrieves a list of commits, or the contents of a specific commit, to provide answers to commit-related questions.                                                                                                                                                                                                                                                                                  | Yes                                                                                                                                                                             | `Explain the changes in the code of this commit`                                                                           |
| **Discussion details**       | Retrieves a specific GitHub discussion. This is useful for quickly getting the gist of the conversation in a discussion.                                                                                                                                                                                                                                                                            | Yes                                                                                                                                                                             | `Summarize this discussion`                                                                                                |
| **File details**             | Retrieves a specific file in the default branch of the Git repository, allowing you to ask questions about the file and the recent changes made to it. This skill is useful when you provide the exact path of a file in the repository.                                                                                                                                                            | Yes                                                                                                                                                                             | <p><code>What logic does user_auth.js encapsulate?</code></p><p><code>What is the file history of user_auth.js?</code></p> |
| **GitHub Advanced Security** | Retrieves information about security alerts within your organization from GitHub Advanced Security features (code scanning, secret scanning, and Dependabot alerts).                                                                                                                                                                                                                                | Yes                                                                                                                                                                             | `How would I fix this code scanning alert?`                                                                                |
| **Issue details**            | Retrieves a specific GitHub issue, including the issue's title, number, author, status, body, linked pull requests, comments, and timestamps.                                                                                                                                                                                                                                                       | Yes                                                                                                                                                                             | `Summarize the conversation on this issue and suggest next steps`                                                          |
| **Lexical code search**      | Keyword code search in the default branch of the Git repository. This skill is useful when you want to know about specific functions, methods or keywords that exist in the code. This skill leverages most of the functionality available to [GitHub Search](https://about/en/search-github/github-code-search/understanding-github-code-search-syntax#using-qualifiers) like `symbol` and `path`. | Yes                                                                                                                                                                             | `Find me the tests for the GitService class`                                                                               |
| **Pull request details**     | Retrieves a specific pull request. This allows you to ask questions about the pull request, including getting a summary of the pull request, its comments, or the code it changes.                                                                                                                                                                                                                  | Yes                                                                                                                                                                             | <p><code>Summarize this PR for me</code></p><p><code>Summarize the changes in this PR</code></p>                           |
| **Release details**          | Retrieves the latest, or specified, release. This allows you to find out who created a release, when it happened, and information included in the release notes.                                                                                                                                                                                                                                    | Yes                                                                                                                                                                             | `When was the latest release?`                                                                                             |
| **Repository details**       | Retrieves a specific GitHub repository. This is useful for finding out details such as the repository owner and the main language used.                                                                                                                                                                                                                                                             | Yes                                                                                                                                                                             | `Tell me about this repo`                                                                                                  |
| **Semantic code search**     | Natural language semantic code search in the default branch of the Git repository. This skill is useful when you want to know where or how certain functionality has been implemented in the code. Note: this requires indexing to be enabled for the repository (see "Indexing repositories for Copilot Chat").                                                                                    | <p>Yes</p><p>Available for all repositories with a Copilot Enterprise subscription, and for public repositories with a Copilot Individual or Copilot Business subscription.</p> | `How does this repo manage HTTP requests and responses?`                                                                   |
| **Support search**           | Retrieves information from the [GitHub Support portal](https://support.github.com/). This skill is useful for asking Copilot Chat about GitHub products and support related questions.                                                                                                                                                                                                              | Yes                                                                                                                                                                             | `Can I use Copilot knowledge bases with Copilot Individual?`                                                               |
| **Web search**               | Searches the web using the Bing search engine. This skill is useful for teaching Copilot about recent events, new developments, trends, technologies, or extremely specific, detailed, or niche subjects.                                                                                                                                                                                           | <p>No</p><p><em>For Copilot Individual:</em><br>Enable in your user settings.</p><p><em>For Copilot Business:</em><br>Enable in organization settings.</p>                      | `What are some recent articles about SAT tokens securing against vulnerabilities in Node?`                                 |

### [AI models for Copilot Chat](broken-reference) <a href="#ai-models-for-copilot-chat" id="ai-models-for-copilot-chat"></a>

Note

Multiple model support in Copilot Chat is in public preview and subject to change.

The following models are currently available through multi-model Copilot Chat:

* **GPT 4o**: This is the default Copilot Chat model. It is a versatile, multimodal model that excels in both text and image processing and is designed to provide fast, reliable responses. It also has superior performance in non-English languages. Learn more about the [model's capabilities](https://platform.openai.com/docs/models/gpt-4o) and review the [model card](https://openai.com/index/gpt-4o-system-card/). Gpt-4o is hosted on Azure.
* **Claude 3.5 Sonnet**: This model excels at coding tasks across the entire software development lifecycle, from initial design to bug fixes, maintenance to optimizations. Learn more about the [model's capabilities](https://www.anthropic.com/claude/sonnet) or read the [model card](https://assets.anthropic.com/m/61e7d27f8c8f5919/original/Claude-3-Model-Card.pdf). GitHub Copilot uses Claude 3.5 Sonnet hosted on Amazon Web Services.
* **o1-preview**: This model is focused on advanced reasoning and solving complex problems, in particular in math and science. It responds more slowly than the `gpt-4o` model. You can make 10 requests to this model per day. Learn more about the [model's capabilities](https://platform.openai.com/docs/models/o1) and review the [model card](https://openai.com/index/openai-o1-system-card/). o1-preview is hosted on Azure.
* **o1-mini**: This is the faster version of the `o1-preview` model, balancing the use of complex reasoning with the need for faster responses. It is best suited for code generation and small context operations. You can make 50 requests to this model per day. Learn more about the [model's capabilities](https://platform.openai.com/docs/models/o1) and review the [model card](https://openai.com/index/openai-o1-system-card/). o1-mini is hosted on Azure.

For more information about the o1 models, see [Models](https://platform.openai.com/docs/models/models) in the OpenAI Platform documentation.

For more information about the Claude 3.5 Sonnet model from Anthropic, see "Using Claude 3.5 Sonnet in GitHub Copilot."

#### [Changing your AI model](broken-reference) <a href="#changing-your-ai-model" id="changing-your-ai-model"></a>

Note

* If you want to use the skills listed in the table above, on the GitHub website, you must use the `gpt-4o` model.
* If you use Copilot Extensions, they may override the model you select.
* Experimental pre-release versions of the models may not interact with all filters correctly, including the duplication detection filter.

1. If you access Copilot Chat through a Copilot Business subscription, your organization must grant members the ability to switch to a different model. See "Managing policies for Copilot in your organization."
2. In the bottom right of any page on GitHub, click .
3. If the panel contains a previous conversation you had with Copilot, in the top right of the panel, click .
4. In the top right of the panel, select the  dropdown menu, then click **Take conversation to immersive**. Multi-model Copilot Chat is currently only available in the immersive view.
5. In the top left of the immersive view, select the **CURRENT-MODEL** dropdown menu, then click the AI model of your choice.

### [Asking a general question about software development](broken-reference) <a href="#asking-a-general-question-about-software-development" id="asking-a-general-question-about-software-development"></a>

You can ask a general question about software development that is not focused on a particular context, such as a repository.

Depending on the question you ask, and your enterprise and organization settings, Copilot may respond using information based on the results of a Bing search. By using Bing search, Copilot can answer a broad range of tech-related questions with up-to-date details based on information currently available on the internet. For information on how to enable or disable Bing search integration, see "[Managing Copilot policies as an individual subscriber](https://about/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/managing-copilot-policies-as-an-individual-subscriber#enabling-or-disabling-web-search-for-github-copilot-chat)" and "Managing policies and features for Copilot in your enterprise."

Note

Bing search integration into Copilot Chat in GitHub is currently in public preview and is subject to change.

1.  On any page on GitHub, click the GitHub Copilot icon at the bottom right of the page.

    The GitHub Copilot Chat panel is displayed. To resize the panel, click and drag the top or left edge.
2. If the panel contains a previous conversation you had with Copilot, click the "New conversation" icon (a plus sign) at the top right of the panel.
3. If the panel is headed "Chatting about OWNER/REPOSITORY," click **All repositories**.
4. If the "Ask Copilot" page is displayed in the panel, click **General purpose chat**.
5.  At the bottom of the panel, in the "Ask Copilot" box, type a question and press Enter.

    Some examples of general questions you could ask are:

    * What are the advantages of the Go programming language?
    * What is Agile software development?
    * What is the most popular JavaScript framework?
    * Give me some examples of regular expressions.
    * Write a bash script to output today's date.
6. Optionally, click  in the text box to stop Copilot from continuing its response.
7. If Copilot uses a Bing search to answer your question, "Results from Bing" is displayed above the response. Click this to see the search results that Copilot used to answer your question.
8.  Within a conversation thread, you can ask follow-up questions. Copilot will answer within the context of the conversation. For example, you could type "tell me more" to get Copilot to expand on its last comment.

    You can use your initial question as a foundation for follow-up questions. A detailed foundational prompt can help Copilot provide more relevant answers to your follow-up questions. For more information, see "[Prompting GitHub Copilot Chat to become your personal AI assistant for accessibility](https://github.blog/2023-10-09-prompting-github-copilot-chat-to-become-your-personal-ai-assistant-for-accessibility/)" on the GitHub Blog.
9. To jump back into a previous conversation you had with Copilot, click the "View conversations" icon (a clock face surrounded by a circular arrow) at the top right of the panel.

### [Asking exploratory questions about a repository](broken-reference) <a href="#asking-exploratory-questions-about-a-repository" id="asking-exploratory-questions-about-a-repository"></a>

Copilot allows you to use natural language questions to explore repositories on GitHub. This can help you get a better understanding of where specific aspects of a codebase are implemented.

1. On the GitHub website, go to the repository you want to chat about.
2.  Click the GitHub Copilot icon at the bottom right of the page.

    The GitHub Copilot Chat panel is displayed. To resize the panel, click and drag the top or left edge.
3.  The heading at the top of the panel should read "Chatting about" followed by the name of the current repository.

    If the wrong repository name is displayed, because you were previously chatting about another repository, click **All repositories** then choose the repository you want to chat about.
4.  In the "Ask Copilot" box, at the bottom of the chat panel, type a question and press Enter.

    For example, you could ask:

    * When was the most recent release?
    * Where is rate limiting implemented in our API?
    * How does the WidgetFactory class work?
    * Where is the code for updating a phone number?
    * Where are SAT tokens generated?
    * Show the most recently updated issues assigned to USERNAME
    * List open issues about SUBJECT
    * What was the last merged PR by USERNAME
    * What are the latest commits to the main branch by USERNAME

    Copilot replies in the chat panel.

    Note

    Copilot's ability to answer natural language questions like these in a repository context is improved when the repository has been indexed for semantic code search. The indexing status of the repository is displayed when you start a conversation that has a repository context. For more information, see "Indexing repositories for Copilot Chat."
5. Optionally, click  in the text box to stop Copilot from continuing its response.
6. To jump back into a previous conversation you had with Copilot, click the "View conversations" icon (a clock face surrounded by a circular arrow) at the top right of the panel.

### [Asking a question about a specific file or symbol](broken-reference) <a href="#asking-a-question-about-a-specific-file-or-symbol" id="asking-a-question-about-a-specific-file-or-symbol"></a>

You can ask Copilot about a specific file or symbol within a repository.

Note

A "symbol" is a named entity in code. This could be a variable, function, class, module, or any other identifier that's part of a codebase.

1.  On any page on GitHub, click the GitHub Copilot icon at the bottom right of the page.

    The GitHub Copilot Chat panel is displayed. To resize the panel, click and drag the top or left edge.
2. If the panel contains a previous conversation you had with Copilot, click the "New conversation" icon (a plus sign) at the top right of the panel.
3. If the "Ask Copilot" page is not displayed in the panel, click **All repositories**.
4.  On the "Ask Copilot" page, select a repository to provide a context for your question.

    For example, you could choose a repository whose code you want to understand better.

    You can search for a repository if you don't see one you want to use.
5. Click the "Attach files or symbols" button (a paperclip icon) at the bottom of the chat panel, then search for and select one or more files and symbols.
6.  In the "Ask Copilot" box, type a question and press Enter.

    Copilot replies in the chat panel.

    Note

    Copilot's ability to answer natural language questions in the context of a repository is improved when the repository has been indexed for semantic code search. The indexing status of the repository is displayed when you start a conversation that has a repository context. For more information, see "Indexing repositories for Copilot Chat."
7. Optionally, click  in the text box to stop Copilot from continuing its response.
8. To jump back into a previous conversation you had with Copilot, click the "View conversations" icon (a clock face surrounded by a circular arrow) at the top right of the panel.

### [Asking questions about specific pieces of code](broken-reference) <a href="#asking-questions-about-specific-pieces-of-code" id="asking-questions-about-specific-pieces-of-code"></a>

You can chat with Copilot about a file in your repository, or about specific lines of code within a file.

1. On GitHub, navigate to a repository and open a file.
2. Do one of the following:
   * To ask a question about the entire file, click the Copilot icon () at the top right of the file view.
   * To ask a question about specific lines within the file:
     1. Select the lines by clicking the line number for the first line you want to select, holding down Shift and clicking the line number for the last line you want to select.
     2. To ask your own question about the selected lines, click the Copilot icon () to the right of your selection. This displays the GitHub Copilot Chat panel with the selected lines indicated as the context of your question.
     3. To ask a predefined question, click the downward-pointing button beside the Copilot icon, then choose one of the options.
3.  If you clicked the Copilot icon, type a question in the "Ask Copilot" box at the bottom of the chat panel and press Enter.

    For example, if you are asking about the entire file, you could enter:

    * Explain this file.
    * How could I improve this code?
    * How can I test this script?

    If you are asking about specific lines, you could enter:

    * Explain the function at the selected lines.
    * How could I improve this class?
    * Add error handling to this code.
    * Write a unit test for this method.

    Copilot responds to your request in the panel.
4. Optionally, click  in the text box to stop Copilot from continuing its response.
5. You can continue the conversation by asking a follow-up question. For example, you could type "tell me more" to get Copilot to expand on its last comment.
6. To clear, delete, or rename the current conversation thread, or to start a new thread, type `/` in the "Ask Copilot" box, select from the options that are displayed, then press Enter.
7. To view a conversation in immersive mode, displaying just the conversation thread, click the dashed box icon at the top right of the conversation thread.

### [Asking questions about GitHub Advanced Security alerts](broken-reference) <a href="#asking-questions-about-github-advanced-security-alerts" id="asking-questions-about-github-advanced-security-alerts"></a>

Copilot allows you to use natural language questions to ask about security alerts in repositories in your organization when these alerts are generated by GitHub Advanced Security features (code scanning, secret scanning, and Dependabot alerts).

1.  On any page on GitHub, click the GitHub Copilot icon at the bottom right of the page.

    The GitHub Copilot Chat panel is displayed. To resize the panel, click and drag the top or left edge.
2. If the panel contains a previous conversation you had with Copilot, click the "New conversation" icon (a plus sign) at the top right of the panel.
3. If the "Ask Copilot" page is not displayed in the panel, click **All repositories**.
4.  On the "Ask Copilot" page, select a repository to provide a context for your question.

    For example, you could choose a repository with security alerts you want to understand better.

    You can search for a repository if you don't see one you want to use.
5.  In the "Ask Copilot" box, type a question and press Enter.

    For example, you could ask:

    * How would I fix this alert?
    * How many alerts do I have on this pull request?
    * Which line of code is this code scanning alert referencing?
    * What library is affected by this Dependabot alert?

    Copilot replies in the chat panel.
6. Optionally, click  in the text box to stop Copilot from continuing its response.
7. To jump back into a previous conversation you had with Copilot, click the "View conversations" icon (a clock face surrounded by a circular arrow) at the top right of the panel.

### [Asking questions about a specific pull request](broken-reference) <a href="#asking-questions-about-a-specific-pull-request" id="asking-questions-about-a-specific-pull-request"></a>

You can ask Copilot to summarize a pull request, or explain what has changed within specific files or lines of code in a pull request.

#### [Get a summary of a pull request](broken-reference) <a href="#get-a-summary-of-a-pull-request" id="get-a-summary-of-a-pull-request"></a>

1. On GitHub, navigate to a pull request in a repository.
2.  At the bottom right of the page, click the GitHub Copilot icon.

    The GitHub Copilot Chat panel is displayed. To resize the panel, click and drag the top or left edge.
3. If the panel contains a previous conversation you had with Copilot, click the plus sign icon at the top right of the Copilot panel to start a new conversation.
4.  At the bottom of the Copilot Chat panel, in the "Ask Copilot" box, type a question and press Enter.

    For example, you could ask:

    * Summarize this PR for me.
    * Summarize the comments in this PR.
    * Summarize the changes in this PR.
5. Optionally, click  in the text box to stop Copilot from continuing its response.

#### [Ask about changes to a specific file in a pull request](broken-reference) <a href="#ask-about-changes-to-a-specific-file-in-a-pull-request" id="ask-about-changes-to-a-specific-file-in-a-pull-request"></a>

1. On GitHub, navigate to a pull request in a repository.
2. Click the **Files changed** tab.
3. Click  at the top right of the file, then click **Ask Copilot about this diff**.
4.  Type a question in the "Ask Copilot" box at the bottom of the chat panel and press Enter.

    For example, you could ask:

    * What's the purpose of this file?
    * Why has this module been included?
5. Optionally, click  in the text box to stop Copilot from continuing its response.

#### [Ask about specific lines within a file in a pull request](broken-reference) <a href="#ask-about-specific-lines-within-a-file-in-a-pull-request" id="ask-about-specific-lines-within-a-file-in-a-pull-request"></a>

1. On GitHub, navigate to a pull request in a repository.
2. Click the **Files changed** tab.
3. Click the line number for the first line you want to select, then hold down Shift and click the line number for the last line you want to select.
4. Ask Copilot a question, or choose from a list of predefined questions.
   *   _To ask your own question about the selected lines_, to the right of your selection, click the Copilot icon. This displays the GitHub Copilot Chat panel with the selected lines indicated as the context of your question.

       For example, you could ask:

       * What is \`actorData\` in this line?
       * Explain this \`do..end\` block.
   * _To ask a predefined question_, to the right of your selection, beside the Copilot icon, click , then click **Explain**.
5. Optionally, click  in the text box to stop Copilot from continuing its response.

#### [Ask why a workflow has failed](broken-reference) <a href="#ask-why-a-workflow-has-failed" id="ask-why-a-workflow-has-failed"></a>

Note

This feature is currently in public preview and subject to change.

1. On GitHub, navigate to a pull request in a repository.
2. Scroll to the bottom of the page, then, next to one of the failing checks, click **Details**.
3.  At the bottom right of the page, click the GitHub Copilot icon.

    The GitHub Copilot Chat panel is displayed. To resize the panel, click and drag the top or left edge.
4. If the panel contains a previous conversation you had with Copilot, click the plus sign icon at the top right of the Copilot panel to start a new conversation.
5.  At the bottom of the Copilot Chat panel, in the "Ask Copilot" box, ask Copilot why the pull request has failed and press Enter.

    For example, you could ask:

    * Tell me why this job failed
    * Suggest a fix for this error

Copilot will respond with information about why the pull request failed. Copilot may also provide suggestions for how to fix the issue.

1. If Copilot has provided steps to fix the issue, you can follow the steps to resolve the problem.
2. Optionally, click  in the text box to stop Copilot from continuing its response.

### [Asking a question about a specific issue or discussion](broken-reference) <a href="#asking-a-question-about-a-specific-issue-or-discussion" id="asking-a-question-about-a-specific-issue-or-discussion"></a>

You can ask Copilot to summarize or answer questions about a specific issue or discussion.

Note

The quality of Copilot Chat's responses may be degraded when working with issues or discussions that have very long bodies or a large number of comments. For example, this may occur if you ask Copilot to summarize a long-running discussion. Where this happens, Copilot will warn you so you can double check its output.

1. Navigate to an issue or discussion on GitHub.
2.  At the bottom right of the page, click the GitHub Copilot icon.

    The GitHub Copilot Chat panel is displayed. To resize the panel, click and drag the top or left edge.
3. If the panel contains a previous conversation you had with Copilot, click the plus sign icon at the top right of the Copilot panel to start a new conversation.
4.  At the bottom of the Copilot chat panel, in the "Ask Copilot" box, type a question and press Enter. For example, you could enter:

    * Explain this issue
    * Summarize this discussion
    * Recommend next steps for this issue
    * What are the acceptance criteria for this issue?
    * What are the main points made by PERSON in this discussion?

    Tip

    Instead of navigating to an issue or discussion in your browser to ask a question, you can include the relevant URL in your message. For example, `Summarize https://github.com/monalisa/octokit/issues/1`.

    Copilot responds to your request in the panel.
5. Optionally, click  in the text box to stop Copilot from continuing its response.

### [Asking a question about a specific commit](broken-reference) <a href="#asking-a-question-about-a-specific-commit" id="asking-a-question-about-a-specific-commit"></a>

You can ask Copilot to explain the changes in a commit.

1. Navigate to a commit on GitHub.
2.  At the bottom right of the page, click the GitHub Copilot icon.

    The GitHub Copilot Chat panel is displayed. To resize the panel, click and drag the top or left edge.
3. If the panel contains a previous conversation you had with Copilot, click the plus sign icon at the top right of the Copilot panel to start a new conversation.
4.  At the bottom of the Copilot chat panel, in the "Ask Copilot" box, type a question and press Enter. For example, you could enter:

    * Summarize the changes in this commit
    * Who committed these changes?
    * When was this commit made?

    Tip

    If you know the SHA for a commit, instead of navigating to the commit, you can ask Copilot about the commit from any page in the repository on GitHub by including the SHA in your message. For example, `What changed in commit a778e0eab?`
5. Optionally, click  in the text box to stop Copilot from continuing its response.

### [Accessing Copilot Chat from the search bar](broken-reference) <a href="#accessing-copilot-chat-from-the-search-bar" id="accessing-copilot-chat-from-the-search-bar"></a>

You can ask Copilot a question about an entire repository by typing your question in the main search box of the repository.

1. Navigate to a repository on GitHub.
2. Press /, or click in the main search box at the top of the page.
3.  In the search box, after `repo:OWNER/REPO`, type the question you want to ask Copilot.

    For example, you could enter:

    * What does this repo do?
    * Where is authentication implemented in this codebase?
    * How does license file detection work in this repo?
4.  Click **Ask Copilot**.

    The GitHub Copilot Chat panel is displayed and Copilot responds to your request.
5. Optionally, click  in the text box to stop Copilot from continuing its response.

### [Extending Copilot Chat in GitHub](broken-reference) <a href="#extending-copilot-chat-in-github" id="extending-copilot-chat-in-github"></a>

Note

GitHub Copilot Extensions is in public preview and subject to change.

GitHub Copilot Extensions integrate the power of external tools into Copilot Chat, helping you reduce context switching and receive responses with domain-specific context. You can install Copilot Extensions from the GitHub Marketplace or build private ones within your organization, then type `@` in a chat window to see a list of your available extensions. To use an extension, select the extension from the list or type the full slug name, then type your prompt.

To learn more, see "Using extensions to integrate external tools with Copilot Chat."

### [Sharing feedback about GitHub Copilot Chat in GitHub](broken-reference) <a href="#sharing-feedback-about-github-copilot-chat-in-github" id="sharing-feedback-about-github-copilot-chat-in-github"></a>

To give feedback about a particular Copilot Chat response, click either the thumbs up or thumbs down icon at the bottom of each chat response.

To give feedback about Copilot Chat in general, click the ellipsis (**...**) at the top right of the chat panel, then click **Give feedback**.

### [Further reading](broken-reference) <a href="#further-reading" id="further-reading"></a>

* "Asking GitHub Copilot questions in your IDE."
* "Asking GitHub Copilot questions in GitHub Mobile."
