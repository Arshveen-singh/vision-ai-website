# Artifact Feature Documentation

## Overview
The Artifact feature provides a structured way to display, manage, and persist generated content like code, documents, images, and charts within VISION AI.

## Components

### 1. Artifact Component (`ai-elements/artifact.tsx`)
A composable component system for displaying artifacts with built-in actions.

**Sub-components:**
- `Artifact` - Main container
- `ArtifactHeader` - Header with title and actions
- `ArtifactTitle` - Title display
- `ArtifactDescription` - Metadata/description text
- `ArtifactActions` - Action buttons container
- `ArtifactAction` - Individual action button
- `ArtifactClose` - Close button
- `ArtifactContent` - Content area

### 2. CodeBlock Component (`ai-elements/code-block.tsx`)
A specialized component for displaying code with syntax highlighting and line numbers.

**Features:**
- Line numbers (optional)
- Language label in header
- Built-in copy button
- Syntax-aware formatting
- Responsive overflow handling
- Dark theme optimized

**Sub-components:**
- `CodeBlock` - Main code display container
- `CodeBlockCopyButton` - Copy to clipboard button

### 3. ArtifactViewer Component
High-level component that uses the Artifact and CodeBlock components to display different types of content.

**Features:**
- Professional code display with line numbers
- Language-specific formatting
- Copy to clipboard (built into CodeBlock for code, separate button for other types)
- Download as file
- Save to workspace
- Share functionality
- Regenerate content
- Run code (for code artifacts)

**Features:**
- Syntax highlighting for code (using react-syntax-highlighter)
- View mode toggle (preview/code)
- Copy to clipboard
- Download as file
- Share functionality
- Save to workspace
- Regenerate content
- Run code (for code artifacts)

**Supported Artifact Types:**
- `code` - Code snippets with syntax highlighting
- `document` - Text documents
- `image` - Images
- `chart` - Charts and visualizations
- `text` - Plain text

## Usage

### Detecting Artifacts in Chat
The `ChatMessage` component automatically detects code blocks in AI responses and renders them as artifacts:

```typescript
// Detects code blocks like:
```python
def hello():
    print("Hello, World!")
```
```

### Creating Artifacts Programmatically
```typescript
const artifact = {
  id: 'artifact_123',
  type: 'code',
  title: 'Python Hello World',
  content: 'def hello():\n    print("Hello, World!")',
  language: 'python',
  metadata: {
    updated: 'just now',
    version: 1
  }
};

<ArtifactViewer 
  artifact={artifact}
  onClose={() => console.log('closed')}
  onRegenerate={() => console.log('regenerate')}
  onRun={() => console.log('run code')}
  onSave={() => console.log('saved')}
/>
```

### Saving Artifacts to Workspace
Artifacts can be saved to persistent workspaces:

1. Click the "Save" button in the artifact viewer
2. Artifact is automatically saved to the active workspace
3. If no workspace exists, a default one is created
4. Saved artifacts persist across sessions

## Backend Integration

### API Endpoints
- `POST /api/v1/desktop/workspace/artifact` - Create artifact
- `PUT /api/v1/desktop/workspace/{workspace_id}/artifact/{artifact_id}` - Update artifact
- `GET /api/v1/desktop/workspace/{workspace_id}/artifact/{artifact_id}` - Get artifact
- `DELETE /api/v1/desktop/workspace/{workspace_id}/artifact/{artifact_id}` - Delete artifact

### Workspace Manager
The `WorkspaceManager` class handles artifact persistence:
- Stores artifacts in `workspaces/{workspace_id}/artifacts/`
- Maintains version history
- Supports metadata and tags

## Styling
Artifacts use Tailwind CSS with the following design principles:
- Dark theme with glass morphism effects
- Border and shadow for depth
- Responsive layout
- Accessible color contrast
- Smooth animations with Framer Motion

## Dependencies
- `framer-motion` - Animations
- `lucide-react` - Icons

All dependencies are already installed. No additional packages required!

## Future Enhancements
- [ ] Code execution in sandboxed environment
- [ ] Real-time collaboration on artifacts
- [ ] Export to multiple formats (PDF, HTML, etc.)
- [ ] Artifact templates
- [ ] Version comparison/diff view
- [ ] Artifact search and filtering
- [ ] Chart/visualization rendering
- [ ] Markdown preview for documents
