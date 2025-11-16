---
description: Generate or update technical documentation with documentation-writer or webdev-documentation-writer
allowed-tools: Read, Write, Edit, Grep, Glob
argument-hint: [type] [target]
---

# Generate Documentation

Create or update technical documentation using documentation-writer or webdev-documentation-writer.

## Process

1. **Identify Documentation Type**
   - README for project overview
   - API docs for endpoints
   - Architecture docs for system design
   - User guide for end users
   - Code comments for complex logic

2. **Gather Context**
   - Read existing code/files
   - Review project structure
   - Understand target audience
   - Identify documentation gaps

3. **Generate Documentation**
   - Invoke documentation-writer (general) or webdev-documentation-writer (web)
   - Create clear, comprehensive docs
   - Include code examples
   - Add diagrams where helpful

4. **Validate Documentation**
   - Test all code examples
   - Verify installation instructions
   - Check for broken links
   - Ensure accuracy

## Arguments

- **$1**: Documentation type (optional, defaults to README)
  - `readme` - Create/update README.md
  - `api` - Generate API documentation
  - `architecture` - Create architecture docs
  - `guide` - Create user guide
  - `comments` - Add inline code comments

- **$2**: Target file or directory (optional)
  - File path for specific documentation
  - Directory for batch documentation

## Examples

```bash
# Create/update project README
/doc readme

# Generate API documentation
/doc api

# Create architecture documentation
/doc architecture

# Document specific module
/doc comments src/models/model.py

# Create user guide
/doc guide
```

## Documentation Types

### README
- Project description
- Installation instructions
- Usage examples
- Configuration options
- Contributing guidelines
- License information

### API Documentation
- Endpoint descriptions
- Request/response schemas
- Authentication requirements
- Error codes
- Code examples (cURL, Python, JavaScript)

### Architecture Documentation
- System overview
- Component diagrams
- Data flow
- Technology stack
- Deployment architecture
- Scaling considerations

### User Guide
- Getting started
- Feature tutorials
- Best practices
- Troubleshooting
- FAQ

### Code Comments
- Function/class documentation
- Complex algorithm explanations
- Design decision rationale
- Edge case handling

## Notes

- Uses documentation-writer for general/ML docs or webdev-documentation-writer for web components/API docs
- Tests all code examples before publishing
- Follows markdown best practices
- Includes diagrams for complex concepts
- Maintains consistent formatting
