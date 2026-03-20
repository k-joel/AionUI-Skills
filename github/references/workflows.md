# GitHub Workflows and Patterns

## Common Git Workflows

### 1. Feature Branch Workflow
```
main (protected)
  │
  ├── feature/login-page
  │     └── commits
  ├── feature/user-profile
  │     └── commits
  └── feature/api-integration
        └── commits
```

**Steps:**
1. Create feature branch from `main`
2. Develop and commit changes
3. Push to remote
4. Create pull request
5. Review and merge
6. Delete feature branch

### 2. GitFlow Workflow
```
main (production)
  │
develop (integration)
  │
  ├── feature/*
  ├── release/*
  └── hotfix/*
```

**Branch types:**
- `main` - Production code
- `develop` - Integration branch
- `feature/*` - New features
- `release/*` - Release preparation
- `hotfix/*` - Production fixes

### 3. Trunk-Based Development
```
main (trunk)
  │
  ├── short-lived feature branches
  │     (merged within 1-2 days)
  └── release branches
        (for versioning)
```

## Pull Request Workflow

### Standard PR Process
1. **Create Branch**
   ```bash
   git checkout -b feature/description
   ```

2. **Make Changes**
   ```bash
   git add .
   git commit -m "feat: add feature"
   ```

3. **Push Branch**
   ```bash
   git push -u origin feature/description
   ```

4. **Create PR**
   - Use GitHub UI or `gh pr create`
   - Add description, reviewers, labels

5. **Address Feedback**
   - Make requested changes
   - Push updates to same branch
   - PR updates automatically

6. **Merge**
   - Squash, merge, or rebase
   - Delete branch (optional)

### PR Templates
Create `.github/PULL_REQUEST_TEMPLATE.md`:
```markdown
## Description
<!-- Describe your changes -->

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests pass
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
```

## Issue Management

### Issue Templates
Create `.github/ISSUE_TEMPLATE/`:
- `bug_report.md`
- `feature_request.md`
- `documentation.md`

### Bug Report Template
```markdown
## Description
<!-- Clear description of the bug -->

## Steps to Reproduce
1. 
2. 
3. 

## Expected Behavior
<!-- What should happen -->

## Actual Behavior
<!-- What actually happens -->

## Environment
- OS: 
- Browser: 
- Version: 

## Additional Context
<!-- Screenshots, logs, etc. -->
```

## Release Management

### Semantic Versioning
- `MAJOR.MINOR.PATCH`
- `1.0.0` - Initial release
- `1.1.0` - New features, backward compatible
- `1.1.1` - Bug fixes

### Release Process
1. Create release branch
2. Update version numbers
3. Update changelog
4. Create tag
5. Build and test
6. Merge to main
7. Create GitHub release

### Changelog Format
```markdown
# Changelog

## [1.1.0] - 2024-01-15
### Added
- New feature X
- API endpoint for Y

### Changed
- Improved performance of Z

### Fixed
- Bug in authentication
```

## CI/CD Workflows

### Basic GitHub Actions Workflow
```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
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
    
    - name: Build
      run: npm run build
```

### Deployment Workflow
```yaml
name: Deploy

on:
  push:
    tags:
      - 'v*'

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Deploy to Production
      run: |
        # Deployment commands
        echo "Deploying version ${GITHUB_REF#refs/tags/}"
```

## Code Review Guidelines

### What to Look For
- **Functionality**: Does it work as intended?
- **Code Quality**: Is it clean and maintainable?
- **Tests**: Are there adequate tests?
- **Security**: Any security concerns?
- **Performance**: Any performance issues?
- **Documentation**: Is it well-documented?

### Review Comments
- Be constructive and specific
- Explain the "why" behind suggestions
- Use code examples when helpful
- Focus on the code, not the person

### Approval Criteria
- All tests pass
- Code follows style guidelines
- No security vulnerabilities
- Documentation updated
- Backward compatibility maintained

## Branch Protection Rules

### Recommended Rules
1. **Require pull request reviews**
   - Number of approvals: 1
   - Dismiss stale approvals
   - Require review from code owners

2. **Require status checks**
   - CI tests must pass
   - Code coverage requirements

3. **Require conversation resolution**
   - All comments addressed

4. **Require signed commits**
   - All commits must be signed

5. **Require linear history**
   - No merge commits allowed

### Configuration
```yaml
# .github/branch-protection.yml
main:
  required_status_checks:
    strict: true
    contexts:
      - "ci/tests"
  required_pull_request_reviews:
    required_approving_review_count: 1
    dismiss_stale_reviews: true
  enforce_admins: false
  required_linear_history: true
  allow_force_pushes: false
  allow_deletions: false
```

## Collaboration Patterns

### Pair Programming via PR
1. Both developers work on same branch
2. Frequent commits and pushes
3. Use PR comments for discussion
4. Both approve before merging

### Mob Programming
1. One driver, many navigators
2. Rotate driver frequently
3. Share screen or use Live Share
4. Single PR for the session

### Open Source Contribution
1. Fork the repository
2. Clone your fork
3. Create feature branch
4. Make changes
5. Push to your fork
6. Create PR to upstream

## Automation Scripts

### Common Automation Tasks
- Auto-assign PR reviewers
- Label issues based on content
- Welcome new contributors
- Stale issue management
- Dependency updates

### Using GitHub Actions for Automation
```yaml
name: Auto Assign
on:
  pull_request:
    types: [opened]

jobs:
  assign:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/github-script@v6
        with:
          script: |
            github.rest.issues.addAssignees({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              assignees: ['team-lead']
            })
```