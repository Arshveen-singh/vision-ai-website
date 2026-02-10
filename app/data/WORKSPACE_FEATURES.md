# Workspace & File Management Features

## Overview
Vision AI now includes persistent workspaces and intuitive file management for complex multimodal projects.

## Features

### 1. Persistent Workspaces
- **Create Multiple Workspaces**: Organize different projects separately
- **Persistent Storage**: All work is saved across sessions
- **Workspace Metadata**: Name, description, creation date, last updated
- **Active Workspace**: Set one workspace as active for current work

### 2. Artifacts Management
- **Generated Content Storage**: Save code, documents, visualizations, charts
- **Version History**: Track changes with automatic versioning
- **Artifact Types**: code, document, image, chart, and more
- **Update & Iterate**: Modify artifacts while preserving history
- **Metadata Support**: Add custom metadata to artifacts

### 3. File Management
- **Drag & Drop Upload**: Simply drag files into the workspace panel
- **Click to Browse**: Traditional file picker also available
- **Multiple File Support**: Upload multiple files at once
- **File Organization**: All files organized by workspace
- **File Types**: Support for images, PDFs, documents, code files, etc.
- **Reference Tracking**: Track how often files are referenced
- **File Metadata**: Size, type, upload date, last accessed

### 4. Intuitive UI
- **Workspace Panel**: Left sidebar for workspace management
- **Collapsible Sections**: Artifacts and Files sections can be expanded/collapsed
- **Visual Indicators**: Icons for different file and artifact types
- **Quick Actions**: Delete, view, and manage items easily
- **Drag-and-Drop Zone**: Visual feedback when dragging files
- **File Size Display**: Human-readable file sizes (KB, MB)

## API Endpoints

### Workspace Management
- `POST /workspace/create` - Create new workspace
- `GET /workspace/list` - List all workspaces
- `GET /workspace/{id}` - Get workspace details
- `POST /workspace/{id}/activate` - Set active workspace
- `DELETE /workspace/{id}` - Delete workspace

### Artifact Management
- `POST /workspace/artifact` - Create artifact
- `PUT /workspace/{id}/artifact/{artifact_id}` - Update artifact
- `GET /workspace/{id}/artifact/{artifact_id}` - Get artifact
- `DELETE /workspace/{id}/artifact/{artifact_id}` - Delete artifact

### File Management
- `POST /workspace/{id}/upload` - Upload file (multipart/form-data)
- `GET /workspace/{id}/files` - List files
- `GET /workspace/{id}/file/{file_id}` - Get file info
- `DELETE /workspace/{id}/file/{file_id}` - Delete file

## Usage Examples

### Creating a Workspace
```typescript
const response = await visionAPI.createWorkspace(
  "My AI Project",
  "Building a chatbot with Vision AI"
);
```

### Uploading Files
```typescript
// Drag and drop automatically handled
// Or programmatically:
const file = new File(["content"], "document.pdf");
await visionAPI.uploadFile(workspaceId, file);
```

### Creating Artifacts
```typescript
await visionAPI.createArtifact(
  workspaceId,
  "code",
  "Main Script",
  "print('Hello World')",
  { language: "python" }
);
```

## Storage Structure
```
workspaces/
├── ws_20250116_143022/
│   ├── metadata.json
│   ├── files_metadata.json
│   ├── files/
│   │   ├── document.pdf
│   │   └── image.png
│   └── artifacts/
│       ├── artifact_0_143045.json
│       └── artifact_1_143102.json
└── ws_20250116_150000/
    └── ...
```

## Benefits
1. **No Lost Work**: Everything persists across sessions
2. **Organized Projects**: Keep different projects separate
3. **Easy File Access**: Reference uploaded files in conversations
4. **Version Control**: Track artifact changes over time
5. **Intuitive UX**: Drag-and-drop makes file management effortless
6. **Cross-Modal**: Files integrate with context awareness system

## Future Enhancements
- Export workspace as ZIP
- Share workspaces with others
- Cloud sync for workspaces
- Advanced search within workspaces
- Workspace templates
- Collaborative editing
