import aiohttp
import asyncio
from config import Colors, TOKEN_FILE

async def validate_single_token(token):
    headers = {"Authorization": token}
    async with aiohttp.ClientSession() as session:
        async with session.get("https://discord.com/api/v10/users/@me", headers=headers) as resp:
            if resp.status == 200:
                data = await resp.json()
                return {
                    "valid": True,
                    "id": data["id"],
                    "username": f"{data['username']}#{data['discriminator']}"
                }
    return {"valid": False}

async def validate_tokens_bulk(file_path=TOKEN_FILE):
    """Validate multiple tokens from file"""
    if not os.path.exists(file_path):
        print(f"{Colors.RED}[-] Token file not found{Colors.RESET}")
        return
    
    valid_tokens = []
    with open(file_path, 'r') as f:
        tokens = [line.strip() for line in f if line.strip()]
    
    print(f"{Colors.CYAN}[+] Validating {len(tokens)} tokens...{Colors.RESET}")
    
    for i, token in enumerate(tokens):
        result = await validate_single_token(token)
        if result["valid"]:
            valid_tokens.append(result)
            print(f"{Colors.GREEN}[+] {result['username']} ({result['id']}){Colors.RESET}")
        else:
            print(f"{Colors.RED}[-] Invalid: {token[:20]}...{Colors.RESET}")
        
        if i % 10 == 0:
            await asyncio.sleep(1)  # Rate limit
    
    print(f"{Colors.YELLOW}[+] {len(valid_tokens)}/{len(tokens)} valid tokens{Colors.RESET}")
    return valid_tokens
