# Artifact Feature - Quick Start Guide

## What are Artifacts?

Artifacts are structured containers for displaying generated content like code, documents, images, and charts. They provide a professional interface with built-in actions for managing the content.

## How to Use

### 1. Generate an Artifact

Simply ask the AI to generate code or content:

**Examples:**
- "Write a Python function to sort a list"
- "Create a JavaScript class for a todo app"
- "Generate a TypeScript interface for a user profile"
- "Write a Java method to calculate factorial"

The AI will respond with a code block, which automatically becomes an artifact.

### 2. Interact with Artifacts

Each artifact has action buttons in the header:

**🔵 Save** - Save artifact to your workspace for later use
**📋 Copy** - Copy content to clipboard
**🔄 Regenerate** - Ask AI to regenerate the content
**⬇️ Download** - Download as a file
**🔗 Share** - Share via Web Share API or copy

### 3. View Modes

For code artifacts, toggle between:
- **👁️ Preview** - Formatted code view
- **💻 Code** - Raw code view

### 4. Manage Saved Artifacts

1. Click the workspace icon in the header
2. View all saved artifacts
3. Click to open and view
4. Delete artifacts you no longer need

## Supported Languages

Artifacts automatically detect and label these languages:
- Python (.py)
- JavaScript (.js)
- TypeScript (.ts)
- Java (.java)
- C++ (.cpp)
- C (.c)
- Rust (.rs)
- Go (.go)
- Ruby (.rb)
- PHP (.php)
- HTML (.html)
- CSS (.css)
- JSON (.json)
- YAML (.yaml)
- Markdown (.md)

## Tips

### Get Better Artifacts
- Be specific about what you want
- Mention the programming language
- Ask for comments and documentation
- Request specific features or patterns

**Good:** "Write a Python function with type hints to calculate fibonacci numbers recursively"
**Better:** "Write a well-documented Python function with type hints and error handling to calculate fibonacci numbers recursively"

### Organize Your Artifacts
- Create workspaces for different projects
- Use descriptive names when saving
- Add metadata/tags for easy searching
- Delete old artifacts to keep things clean

### Keyboard Shortcuts
- `Ctrl+C` / `Cmd+C` - Copy artifact content
- `Ctrl+S` / `Cmd+S` - Save to workspace (when focused)
- `Esc` - Close artifact viewer

## Examples

### Example 1: Python Function
**Prompt:** "Write a Python function to validate email addresses"

**Result:** Artifact with:
- Title: "Python Code"
- Language: python
- Actions: Save, Copy, Regenerate, Download, Share
- Content: Formatted Python code

### Example 2: JavaScript Class
**Prompt:** "Create a JavaScript class for managing a shopping cart"

**Result:** Artifact with:
- Title: "JavaScript Code"
- Language: javascript
- Actions: Save, Copy, Regenerate, Download, Share
- Content: Formatted JavaScript code

### Example 3: Multiple Artifacts
**Conversation:**
1. "Write a Python API client"
2. "Now write tests for that client"
3. "Add error handling"

**Result:** Three separate artifacts, each with independent actions

## Troubleshooting

### Artifact Not Appearing
- Ensure code is in a code block (triple backticks)
- Specify the language: \`\`\`python
- Check browser console for errors

### Save Button Not Working
- Verify backend is running
- Check API key is configured
- Ensure workspace feature is enabled

### Copy Not Working
- Check browser clipboard permissions
- Use HTTPS or localhost
- Try the Download button instead

## Advanced Usage

### Custom Metadata
When saving artifacts programmatically:
```typescript
visionAPI.createArtifact(
  workspaceId,
  'code',
  'My Function',
  codeContent,
  {
    author: 'AI',
    tags: ['python', 'utility'],
    version: '1.0'
  }
);
```

### Version History
Artifacts maintain version history:
- Each update creates a new version
- Previous versions are preserved
- View version history in workspace panel

### Artifact Types
- `code` - Code snippets
- `document` - Text documents
- `image` - Images
- `chart` - Charts and visualizations
- `text` - Plain text

## Best Practices

1. **Save Important Code** - Don't lose valuable generated code
2. **Use Descriptive Titles** - Make artifacts easy to find
3. **Organize by Project** - Create separate workspaces
4. **Review Before Using** - Always review generated code
5. **Add Comments** - Ask AI to add explanatory comments
6. **Test Generated Code** - Verify functionality before production use

## Need Help?

- Check the full documentation: `docs/ARTIFACT_FEATURE.md`
- Run tests: `electron-app/TEST_ARTIFACT.md`
- Report issues: GitHub Issues
- Ask the AI: "How do I use artifacts?"

---

**Happy Coding! 🚀**
