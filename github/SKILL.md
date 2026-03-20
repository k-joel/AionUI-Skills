---
name: github
description: Comprehensive GitHub operations including repository management, commits, pull requests, issues, and GitHub API interactions. Use when the user needs to perform any GitHub-related tasks such as creating repositories, pushing commits, managing branches, creating pull requests, managing issues, or working with GitHub Actions. This skill provides both command-line and API-based approaches for GitHub operations.
---

# GitHub Operations Skill

This skill provides comprehensive guidance for performing GitHub operations including repository management, commits, branches, pull requests, issues, and GitHub API interactions.

## Quick Start

### Authentication
GitHub operations require authentication. Use one of these methods:

1. **Personal Access Token (PAT)** - Recommended for API operations
2. **GitHub CLI (`gh`)** - For command-line operations
3. **SSH Keys** - For git operations

### Basic Workflow
1. Authenticate with GitHub
2. Perform the required operation (create repo, push code, etc.)
3. Verify the operation completed successfully

## Repository Operations

### Creating a Repository

**Using GitHub CLI:**
```bash
gh repo create my-test-repo --public --description "My test repository"
```

**Using GitHub API (curl):**
```bash
curl -X POST -H "Authorization: token YOUR_PAT" 
  -H "Accept: application/vnd.github.v3+json" 
  https://api.github.com/user/repos 
  -d '{"name":"my-test-repo","description":"My test repository","private":false}'
```

### Cloning a Repository
```bash
git clone https://github.com/username/repository.git
# or with SSH
git clone git@github.com:username/repository.git
```

## Git Operations

### Initializing and Committing
```bash
# Initialize repository
git init

# Add files
git add .

# Commit changes
git commit -m "Initial commit"

# Set remote origin
git remote add origin https://github.com/username/repository.git

# Push to GitHub
git push -u origin main
```

### Branch Management
```bash
# Create new branch
git checkout -b feature-branch

# Switch branches
git checkout main

# Merge branches
git merge feature-branch

# Delete branch
git branch -d feature-branch
```

## Pull Requests

### Creating a Pull Request
```bash
# Using GitHub CLI
gh pr create --title "Feature implementation" --body "Description of changes"

# List pull requests
gh pr list

# View specific PR
gh pr view 123
```

### Reviewing and Merging
```bash
# Review PR
gh pr review 123 --approve --body "Looks good!"

# Merge PR
gh pr merge 123 --squash
```

## Issues Management

### Creating Issues
```bash
gh issue create --title "Bug report" --body "Description of the bug"
```

### Listing and Managing Issues
```bash
# List issues
gh issue list

# View issue
gh issue view 456

# Close issue
gh issue close 456 --comment "Fixed in PR #123"
```

## GitHub API Operations

### Common API Endpoints

- **User repos**: `GET /user/repos`
- **Create repo**: `POST /user/repos`
- **Get repo**: `GET /repos/{owner}/{repo}`
- **Create issue**: `POST /repos/{owner}/{repo}/issues`
- **Create PR**: `POST /repos/{owner}/{repo}/pulls`

### API Authentication Headers
```bash
# For PAT authentication
-H "Authorization: token YOUR_PAT"
-H "Accept: application/vnd.github.v3+json"

# For GitHub App authentication
-H "Authorization: Bearer YOUR_JWT"
```

## GitHub Actions

### Basic Workflow File
```yaml
name: CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Setup Node.js
      uses: actions/setup-node@v4
      with:
        node-version: '20'
    
    - name: Install dependencies
      run: npm ci
    
    - name: Run tests
      run: npm test
```

## Security Best Practices

1. **Never commit secrets** - Use GitHub Secrets for sensitive data
2. **Use .gitignore** - Exclude sensitive files and build artifacts
3. **Branch protection** - Enable branch protection rules for main branch
4. **Code scanning** - Enable GitHub Code Scanning for security analysis
5. **Dependabot** - Enable Dependabot for dependency updates

## Troubleshooting

### Common Issues

1. **Authentication failed** - Verify PAT has correct permissions
2. **Permission denied** - Check repository access rights
3. **Merge conflicts** - Resolve conflicts before pushing
4. **Large files** - Use Git LFS for large files

### Debugging Commands
```bash
# Check git status
git status

# View git log
git log --oneline

# Check remote URLs
git remote -v

# Test GitHub CLI authentication
gh auth status
```

## Scripts

This skill includes Python scripts for common GitHub operations. See the `scripts/` directory for:
- `create_repo.py` - Create repositories programmatically
- `push_commit.py` - Commit and push changes
- `create_pr.py` - Create pull requests

## References

See the `references/` directory for:
- `api-reference.md` - Complete GitHub API reference
- `permissions.md` - Required permissions for different operations
- `workflows.md` - Common GitHub workflows and patterns