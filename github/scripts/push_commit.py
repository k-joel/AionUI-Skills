#!/usr/bin/env python3
"""
Git Commit and Push Script

This script automates the process of committing and pushing changes to a GitHub repository.

Usage:
    python push_commit.py --repo-path <path> --message <commit-message> [--branch <branch>]

Example:
    python push_commit.py --repo-path ./my-project --message "Initial commit" --branch main
"""

import argparse
import subprocess
import os
import sys

def run_command(command, cwd=None):
    """Run a shell command and return output."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            cwd=cwd,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    except subprocess.CalledProcessError as e:
        return e.stdout.strip(), e.stderr.strip(), e.returncode

def check_git_installed():
    """Check if git is installed and available."""
    stdout, stderr, returncode = run_command("git --version")
    if returncode != 0:
        print("❌ Git is not installed or not in PATH")
        return False
    print(f"✅ Git version: {stdout}")
    return True

def is_git_repository(path):
    """Check if the given path is a git repository."""
    git_dir = os.path.join(path, ".git")
    return os.path.exists(git_dir)

def initialize_git_repo(path):
    """Initialize a new git repository."""
    print(f"Initializing git repository in {path}")
    
    # Initialize git
    stdout, stderr, returncode = run_command("git init", cwd=path)
    if returncode != 0:
        print(f"❌ Failed to initialize git: {stderr}")
        return False
    
    # Create initial README
    readme_path = os.path.join(path, "README.md")
    if not os.path.exists(readme_path):
        with open(readme_path, "w") as f:
            f.write(f"# {os.path.basename(path)}

Project description goes here.
")
    
    return True

def commit_and_push(path, commit_message, branch="main"):
    """Commit changes and push to remote."""
    
    # Check if repository exists
    if not is_git_repository(path):
        print(f"❌ Not a git repository: {path}")
        choice = input("Initialize as new git repository? (y/n): ")
        if choice.lower() == 'y':
            if not initialize_git_repo(path):
                return False
        else:
            return False
    
    # Add all files
    print("Adding files to git...")
    stdout, stderr, returncode = run_command("git add .", cwd=path)
    if returncode != 0:
        print(f"❌ Failed to add files: {stderr}")
        return False
    
    # Check if there are changes to commit
    stdout, stderr, returncode = run_command("git status --porcelain", cwd=path)
    if not stdout:
        print("⚠️ No changes to commit")
        return True
    
    # Commit changes
    print(f"Committing changes with message: '{commit_message}'")
    stdout, stderr, returncode = run_command(f'git commit -m "{commit_message}"', cwd=path)
    if returncode != 0:
        print(f"❌ Failed to commit: {stderr}")
        return False
    print(f"✅ Committed: {stdout}")
    
    # Check if remote is set
    stdout, stderr, returncode = run_command("git remote -v", cwd=path)
    if not stdout:
        print("⚠️ No remote repository set. Commit was successful locally.")
        print("   To set a remote: git remote add origin <url>")
        print("   Then push: git push -u origin main")
        return True
    
    # Push to remote
    print(f"Pushing to remote repository...")
    stdout, stderr, returncode = run_command(f"git push -u origin {branch}", cwd=path)
    if returncode != 0:
        print(f"❌ Failed to push: {stderr}")
        
        # Try to set upstream if not set
        if "no upstream branch" in stderr.lower():
            print("Setting upstream branch...")
            stdout, stderr, returncode = run_command(f"git push --set-upstream origin {branch}", cwd=path)
            if returncode != 0:
                print(f"❌ Still failed to push: {stderr}")
                return False
        
    print(f"✅ Successfully pushed to {branch}")
    return True

def main():
    parser = argparse.ArgumentParser(description="Commit and push changes to git repository")
    parser.add_argument("--repo-path", required=True, help="Path to git repository")
    parser.add_argument("--message", required=True, help="Commit message")
    parser.add_argument("--branch", default="main", help="Branch name (default: main)")
    
    args = parser.parse_args()
    
    # Check if git is installed
    if not check_git_installed():
        return 1
    
    # Check if path exists
    if not os.path.exists(args.repo_path):
        print(f"❌ Path does not exist: {args.repo_path}")
        return 1
    
    # Commit and push
    success = commit_and_push(args.repo_path, args.message, args.branch)
    
    if success:
        print("
🎉 Successfully committed and pushed changes!")
        return 0
    else:
        print("
❌ Failed to commit and push changes.")
        return 1

if __name__ == "__main__":
    sys.exit(main())