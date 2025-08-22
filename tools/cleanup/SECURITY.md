# SECURITY NOTICE - IMPORTANT

## ⚠️ API Key Security

**This is a PUBLIC repository. NEVER commit API keys or credentials!**

### What NOT to do:
- ❌ Never hardcode API keys in any `.py`, `.ps1`, `.bat`, or `.md` files
- ❌ Never pass API keys as command line arguments in documentation
- ❌ Never commit `.api_key`, `.env`, or credential files
- ❌ Never share scripts with embedded keys

### What TO do:
- ✅ Use environment variables for credentials
- ✅ Store keys in gitignored files (`.api_key`)
- ✅ Use the `setup_credentials.bat` script for configuration
- ✅ Always check files before committing

## Setting Up Credentials Safely

### Method 1: Environment Variables (Recommended)
```powershell
# PowerShell (temporary - current session only)
$env:CUSTOM_LLM_API_KEY = "your-key-here"

# Windows CMD (temporary)
set CUSTOM_LLM_API_KEY=your-key-here

# Permanent (Windows)
setx CUSTOM_LLM_API_KEY "your-key-here"
```

### Method 2: Untracked Config File
```bash
# Create a gitignored file
echo "your-api-key" > tools\cleanup\.api_key
```

### Method 3: Use Setup Script
```bash
tools\cleanup\setup_credentials.bat
```

## Files That Are Gitignored

The following files/patterns are automatically ignored:
- `.api_key`
- `*.api_key`
- `api_key.txt`
- `credentials.txt`
- `config.ini`
- `.env`
- `.env.local`

## If You Accidentally Commit a Key

If you accidentally commit an API key:

1. **Immediately revoke the key** in your API provider's dashboard
2. Remove the key from the repository:
   ```bash
   # Remove from current commit
   git rm --cached file-with-key.txt
   git commit -m "Remove exposed credentials"
   
   # For historical commits, use git filter-branch or BFG Repo-Cleaner
   ```
3. Generate a new API key
4. Update your local configuration with the new key
5. Never use the exposed key again

## Checking for Exposed Keys

Before committing, always check:
```bash
# Search for potential keys in staged files
git diff --staged | grep -E "(api[_-]?key|token|secret|password)" -i

# List all tracked files that might contain keys
git ls-files | xargs grep -l "sk-" 2>/dev/null
```

## Best Practices

1. **Use a pre-commit hook** to check for credentials
2. **Review all changes** before pushing to GitHub
3. **Use secret scanning** tools if available
4. **Rotate keys regularly** as a security practice
5. **Limit key permissions** to only what's needed
6. **Use different keys** for development and production

## Contact

If you discover any security issues or exposed credentials in this repository, please report them immediately by:
1. Opening a private security advisory on GitHub
2. Do NOT open a public issue with credential details

Remember: **Security is everyone's responsibility!**