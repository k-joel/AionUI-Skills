# GitHub API Reference

## Authentication

### Personal Access Token (PAT)
```bash
curl -H "Authorization: token ghp_your_token" 
  -H "Accept: application/vnd.github.v3+json" 
  https://api.github.com/user
```

### GitHub App Installation Token
```bash
curl -H "Authorization: Bearer your_jwt_token" 
  -H "Accept: application/vnd.github.v3+json" 
  https://api.github.com/app/installations
```

## Repository Endpoints

### Create Repository
```bash
POST /user/repos
POST /orgs/{org}/repos

# Request body
{
  "name": "repo-name",
  "description": "Repository description",
  "private": false,
  "auto_init": true,
  "gitignore_template": "Python",
  "license_template": "mit"
}
```

### Get Repository
```bash
GET /repos/{owner}/{repo}

# Response includes:
# - html_url, clone_url, ssh_url
# - default_branch
# - permissions
# - visibility (public/private)
```

### List User Repositories
```bash
GET /user/repos
# Parameters: type (all, owner, member), sort, direction
```

## Branch Operations

### Get Branch
```bash
GET /repos/{owner}/{repo}/branches/{branch}
```

### Create Branch
```bash
POST /repos/{owner}/{repo}/git/refs

# Request body
{
  "ref": "refs/heads/feature-branch",
  "sha": "commit_sha"
}
```

## Commit Operations

### Create Commit
```bash
POST /repos/{owner}/{repo}/git/commits

{
  "message": "Commit message",
  "tree": "tree_sha",
  "parents": ["parent_sha"]
}
```

### Get Commit
```bash
GET /repos/{owner}/{repo}/commits/{sha}
```

## Pull Request Endpoints

### Create Pull Request
```bash
POST /repos/{owner}/{repo}/pulls

{
  "title": "PR Title",
  "body": "PR Description",
  "head": "feature-branch",
  "base": "main"
}
```

### List Pull Requests
```bash
GET /repos/{owner}/{repo}/pulls
# Parameters: state (open, closed, all), sort, direction
```

### Merge Pull Request
```bash
PUT /repos/{owner}/{repo}/pulls/{pull_number}/merge

{
  "commit_message": "Merge PR",
  "merge_method": "merge|squash|rebase"
}
```

## Issues Endpoints

### Create Issue
```bash
POST /repos/{owner}/{repo}/issues

{
  "title": "Issue title",
  "body": "Issue description",
  "labels": ["bug", "enhancement"],
  "assignees": ["username"]
}
```

### List Issues
```bash
GET /repos/{owner}/{repo}/issues
# Parameters: state, labels, sort, direction
```

## Webhooks

### Create Webhook
```bash
POST /repos/{owner}/{repo}/hooks

{
  "name": "web",
  "active": true,
  "events": ["push", "pull_request"],
  "config": {
    "url": "https://example.com/webhook",
    "content_type": "json"
  }
}
```

## Rate Limiting

- **Unauthenticated**: 60 requests per hour
- **Authenticated**: 5,000 requests per hour
- **Check limits**: `GET /rate_limit`

## Common Response Codes

- `200` - Success
- `201` - Created
- `204` - No Content
- `400` - Bad Request
- `401` - Unauthorized
- `403` - Forbidden
- `404` - Not Found
- `422` - Validation Failed
- `429` - Rate Limit Exceeded

## Pagination

GitHub API responses are paginated (30 items per page by default).

```bash
# Link headers in response
Link: <https://api.github.com/user/repos?page=2>; rel="next",
      <https://api.github.com/user/repos?page=5>; rel="last"

# Query parameters
?page=2&per_page=100
```

## GraphQL API

GitHub also provides a GraphQL API at `https://api.github.com/graphql`.

```graphql
query {
  repository(owner: "octocat", name: "Hello-World") {
    name
    description
    stargazers {
      totalCount
    }
  }
}
```