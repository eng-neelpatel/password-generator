#!/usr/bin/env python3
"""
Password Generator CLI Tool
Generates secure random passwords with customizable options.
"""

import random
import string
import argparse
import sys


class PasswordGenerator:
    """A class to generate secure random passwords."""
    
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = string.punctuation
    
    def generate(self, length=12, use_uppercase=True, use_digits=True, 
                 use_symbols=True, exclude_similar=False):
        """
        Generate a random password based on specified criteria.
        
        Args:
            length (int): Length of the password (default: 12)
            use_uppercase (bool): Include uppercase letters (default: True)
            use_digits (bool): Include digits (default: True)
            use_symbols (bool): Include special symbols (default: True)
            exclude_similar (bool): Exclude similar characters like 'l', '1', 'O', '0' (default: False)
        
        Returns:
            str: Generated password
        """
        if length < 4:
            raise ValueError("Password length must be at least 4 characters")
        
        # Build character pool
        char_pool = self.lowercase
        
        if use_uppercase:
            char_pool += self.uppercase
        if use_digits:
            char_pool += self.digits
        if use_symbols:
            char_pool += self.symbols
        
        # Remove similar characters if requested
        if exclude_similar:
            similar_chars = 'il1Lo0O'
            char_pool = ''.join(c for c in char_pool if c not in similar_chars)
        
        # Ensure at least one character from each selected category
        password = []
        if use_uppercase:
            password.append(random.choice(self.uppercase))
        if use_digits:
            password.append(random.choice(self.digits))
        if use_symbols:
            password.append(random.choice(self.symbols))
        password.append(random.choice(self.lowercase))
        
        # Fill remaining length with random characters
        remaining_length = length - len(password)
        password.extend(random.choice(char_pool) for _ in range(remaining_length))
        
        # Shuffle to avoid predictable patterns
        random.shuffle(password)
        
        return ''.join(password)
    
    def generate_multiple(self, count=5, **kwargs):
        """
        Generate multiple passwords.
        
        Args:
            count (int): Number of passwords to generate
            **kwargs: Arguments to pass to generate() method
        
        Returns:
            list: List of generated passwords
        """
        return [self.generate(**kwargs) for _ in range(count)]


def main():
    """Main function to handle CLI arguments and generate passwords."""
    parser = argparse.ArgumentParser(
        description='Generate secure random passwords',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate a default 12-character password
  python password_generator.py
  
  # Generate a 16-character password
  python password_generator.py -l 16
  
  # Generate 5 passwords without symbols
  python password_generator.py -n 5 --no-symbols
  
  # Generate password without similar characters
  python password_generator.py --exclude-similar
        """
    )
    
    parser.add_argument(
        '-l', '--length',
        type=int,
        default=12,
        help='Length of the password (default: 12)'
    )
    parser.add_argument(
        '-n', '--number',
        type=int,
        default=1,
        help='Number of passwords to generate (default: 1)'
    )
    parser.add_argument(
        '--no-uppercase',
        action='store_true',
        help='Exclude uppercase letters'
    )
    parser.add_argument(
        '--no-digits',
        action='store_true',
        help='Exclude digits'
    )
    parser.add_argument(
        '--no-symbols',
        action='store_true',
        help='Exclude special symbols'
    )
    parser.add_argument(
        '--exclude-similar',
        action='store_true',
        help='Exclude similar characters (l, 1, O, 0, etc.)'
    )
    
    args = parser.parse_args()
    
    # Validate length
    if args.length < 4:
        print("Error: Password length must be at least 4 characters", file=sys.stderr)
        sys.exit(1)
    
    # Create generator and generate passwords
    generator = PasswordGenerator()
    
    try:
        if args.number == 1:
            password = generator.generate(
                length=args.length,
                use_uppercase=not args.no_uppercase,
                use_digits=not args.no_digits,
                use_symbols=not args.no_symbols,
                exclude_similar=args.exclude_similar
            )
            print(password)
        else:
            passwords = generator.generate_multiple(
                count=args.number,
                length=args.length,
                use_uppercase=not args.no_uppercase,
                use_digits=not args.no_digits,
                use_symbols=not args.no_symbols,
                exclude_similar=args.exclude_similar
            )
            for i, pwd in enumerate(passwords, 1):
                print(f"{i}. {pwd}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
