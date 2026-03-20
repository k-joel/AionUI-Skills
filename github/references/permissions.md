# GitHub Permissions Guide

## Personal Access Token (PAT) Scopes

### Repository Scopes
- **repo** - Full control of private and public repositories
- **repo:status** - Access commit status
- **repo_deployment** - Access deployment status
- **public_repo** - Access public repositories only
- **repo:invite** - Accept repository invitations
- **security_events** - Read and write security events

### Organization Scopes
- **admin:org** - Full organization administration
- **write:org** - Read and write organization membership
- **read:org** - Read organization membership

### User Scopes
- **user** - Update ALL user data
- **read:user** - Read user profile data
- **user:email** - Access user email addresses
- **user:follow** - Follow and unfollow users

### Gist Scopes
- **gist** - Create, update, delete, and list gists

### Notification Scopes
- **notifications** - Access notifications

### Project Scopes
- **project** - Read and write projects
- **read:project** - Read projects only

### Package Scopes
- **write:packages** - Upload packages
- **read:packages** - Download packages
- **delete:packages** - Delete packages

### GitHub Actions Scopes
- **workflow** - Add and update GitHub Actions workflow files

## Minimum Required Scopes for Common Operations

### Create Public Repository
- `public_repo` (or `repo` for both public and private)

### Create Private Repository
- `repo`

### Push Code to Repository
- `repo` (for private repos)
- `public_repo` (for public repos)

### Create Issues
- `repo` (for private repos)
- `public_repo` (for public repos)

### Create Pull Requests
- `repo` (for private repos)
- `public_repo` (for public repos)

### Read Repository Contents
- `repo` (for private repos)
- No scope needed for public repos

### Manage Organization Repositories
- `admin:org` or `write:org`

### Access User Email
- `user:email`

## Fine-grained Personal Access Tokens

Fine-grained PATs provide more granular control:

### Repository Access
- **No access** - Cannot access the repository
- **Read-only** - Can read repository contents
- **Read and write** - Can read and write to repository
- **Administrator** - Full administrative access

### Repository Permissions
- **Contents** - Read/write repository contents
- **Metadata** - Read/write repository metadata
- **Pull requests** - Read/write pull requests
- **Issues** - Read/write issues
- **Actions** - Read/write GitHub Actions
- **Secrets** - Read/write secrets
- **Environments** - Read/write environments
- **Pages** - Read/write GitHub Pages
- **Discussions** - Read/write discussions

### Organization Permissions
- **Members** - Read/write organization members
- **Projects** - Read/write organization projects

## GitHub App Permissions

GitHub Apps can request specific permissions:

### Repository Permissions
- **Administration** - Repository administration
- **Contents** - Repository contents
- **Issues** - Issues
- **Pull requests** - Pull requests
- **Metadata** - Repository metadata

### Organization Permissions
- **Members** - Organization members
- **Projects** - Organization projects

## Best Practices

### 1. Principle of Least Privilege
- Grant only the permissions needed for the task
- Use fine-grained tokens when possible
- Regularly review and rotate tokens

### 2. Token Security
- Never commit tokens to version control
- Use environment variables or secret managers
- Set expiration dates on tokens
- Monitor token usage

### 3. Organization Security
- Use GitHub Organizations for team management
- Implement branch protection rules
- Require code review for sensitive branches
- Enable security scanning

### 4. Audit and Monitoring
- Regularly review audit logs
- Monitor for unusual activity
- Set up alerts for security events
- Review installed GitHub Apps

## Common Permission Errors

### "Resource not accessible by integration"
The token doesn't have required permissions. Check token scopes.

### "Bad credentials"
Token is invalid or expired. Generate a new token.

### "Requires authentication"
No token provided or token doesn't have required scope.

### "Not found"
Resource doesn't exist or token doesn't have access.

## Token Management Commands

### Check Token Scopes
```bash
curl -H "Authorization: token YOUR_TOKEN" 
  https://api.github.com/rate_limit
```

### Revoke Token
Go to GitHub Settings → Developer settings → Personal access tokens

### Create New Token
GitHub Settings → Developer settings → Personal access tokens → Generate new token