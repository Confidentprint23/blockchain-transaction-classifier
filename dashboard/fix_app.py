# fix_app.py - Quick fix for the range error

import re

print("🔧 Fixing app.py range error...")

# Read the current app.py
with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the problematic line
old_line = "network_sizes = range(1000, 20000, 1000)"
new_line = "network_sizes = list(range(1000, 20000, 1000))"

if old_line in content:
    content = content.replace(old_line, new_line)
    print(f"✅ Found and fixed: {old_line}")
    
    # Backup original
    with open('app.py.backup', 'w', encoding='utf-8') as f:
        with open('app.py', 'r', encoding='utf-8') as orig:
            f.write(orig.read())
    print("📦 Backup saved as app.py.backup")
    
    # Save fixed version
    with open('app.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("✅ app.py has been fixed!")
else:
    print("⚠️ Line not found. Searching for similar patterns...")
    
    # Try alternative search
    pattern = r'network_sizes\s*=\s*range\('
    if re.search(pattern, content):
        content = re.sub(pattern, 'network_sizes = list(range(', content)
        with open('app.py', 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ Fixed using pattern matching!")
    else:
        print("❌ Could not find the error. Manual fix needed.")

print("\n🎯 Next step: Restart Streamlit")
print("   streamlit run app.py")