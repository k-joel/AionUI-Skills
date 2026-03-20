#!/usr/bin/env python3
"""
GitHub Repository Creator

This script creates a new GitHub repository using the GitHub API.
Requires a GitHub Personal Access Token (PAT) with repo permissions.

Usage:
    python create_repo.py --token <PAT> --name <repo-name> [--description <description>] [--private]

Example:
    python create_repo.py --token ghp_abc123 --name my-test-repo --description "Test repository" --public
"""

import argparse
import requests
import sys
import json

def create_github_repository(token, repo_name, description="", private=False):
    """
    Create a new GitHub repository.
    
    Args:
        token (str): GitHub Personal Access Token
        repo_name (str): Name of the repository to create
        description (str): Repository description
        private (bool): Whether the repository should be private
    
    Returns:
        dict: Repository information if successful, None if failed
    """
    url = "https://api.github.com/user/repos"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json"
    }
    
    data = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": True,  # Initialize with README
        "gitignore_template": "Python"  # Add .gitignore for Python
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        
        repo_info = response.json()
        print(f"✅ Repository created successfully!")
        print(f"   Name: {repo_info['name']}")
        print(f"   URL: {repo_info['html_url']}")
        print(f"   SSH URL: {repo_info['ssh_url']}")
        print(f"   Clone URL: {repo_info['clone_url']}")
        print(f"   Private: {repo_info['private']}")
        
        return repo_info
        
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e}")
        if response.status_code == 401:
            print("   Authentication failed. Check your PAT token.")
        elif response.status_code == 422:
            print("   Repository might already exist or name is invalid.")
            error_data = response.json()
            if 'errors' in error_data:
                for error in error_data['errors']:
                    print(f"   - {error.get('message', 'Unknown error')}")
        else:
            print(f"   Status code: {response.status_code}")
            print(f"   Response: {response.text}")
        return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Create a GitHub repository")
    parser.add_argument("--token", required=True, help="GitHub Personal Access Token")
    parser.add_argument("--name", required=True, help="Repository name")
    parser.add_argument("--description", default="", help="Repository description")
    parser.add_argument("--private", action="store_true", help="Make repository private (default: public)")
    
    args = parser.parse_args()
    
    print(f"Creating repository: {args.name}")
    print(f"Description: {args.description}")
    print(f"Visibility: {'Private' if args.private else 'Public'}")
    
    result = create_github_repository(
        token=args.token,
        repo_name=args.name,
        description=args.description,
        private=args.private
    )
    
    if result:
        print("
🎉 Repository created successfully!")
        print(f"🔗 Browse: {result['html_url']}")
        print(f"📋 Clone: git clone {result['clone_url']}")
        return 0
    else:
        print("
❌ Failed to create repository.")
        return 1

if __name__ == "__main__":
    sys.exit(main())