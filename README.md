# Password Generator

A secure and customizable password generator CLI tool built with Python. Generate strong, random passwords with various options to meet your security requirements.

## Features

- 🔐 Generate secure random passwords
- 📏 Customizable password length
- 🔤 Toggle uppercase letters, digits, and special symbols
- 👁️ Option to exclude similar-looking characters (l, 1, O, 0, etc.)
- 🔢 Generate multiple passwords at once
- ⚡ Fast and lightweight
- 💻 Easy-to-use command-line interface

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/eng-neelpatel/password-generator.git
cd password-generator
```

2. Make the script executable (optional, Linux/Mac):
```bash
chmod +x password_generator.py
```

## Usage

### Basic Usage

Generate a default 12-character password:
```bash
python password_generator.py
```

Output example:
```
K9$mN2pL#xQ7
```

### Custom Length

Generate a 16-character password:
```bash
python password_generator.py -l 16
```
or
```bash
python password_generator.py --length 16
```

### Generate Multiple Passwords

Generate 5 passwords at once:
```bash
python password_generator.py -n 5
```

Output example:
```
1. mK8#pL2xQ9$N
2. R7@nP5wM3&Lq
3. T4*vB9yH6#Jk
4. W2!cD8xF5@Zn
5. G3%hM7tK4$Vp
```

### Exclude Character Types

Generate password without symbols:
```bash
python password_generator.py --no-symbols
```

Generate password without uppercase letters:
```bash
python password_generator.py --no-uppercase
```

Generate password without digits:
```bash
python password_generator.py --no-digits
```

### Exclude Similar Characters

Generate password excluding similar-looking characters:
```bash
python password_generator.py --exclude-similar
```

### Combine Options

Generate 3 passwords, each 20 characters long, without symbols:
```bash
python password_generator.py -n 3 -l 20 --no-symbols
```

## Command-Line Options

| Option | Short | Description | Default |
|--------|-------|-------------|--------|
| `--length` | `-l` | Length of the password | 12 |
| `--number` | `-n` | Number of passwords to generate | 1 |
| `--no-uppercase` | | Exclude uppercase letters | False |
| `--no-digits` | | Exclude digits | False |
| `--no-symbols` | | Exclude special symbols | False |
| `--exclude-similar` | | Exclude similar characters (l, 1, O, 0) | False |
| `--help` | `-h` | Show help message | |

## Examples

```bash
# Generate a simple 8-character password with only lowercase and digits
python password_generator.py -l 8 --no-uppercase --no-symbols

# Generate 10 easy-to-read passwords (no similar characters)
python password_generator.py -n 10 --exclude-similar

# Generate a very strong 32-character password
python password_generator.py -l 32

# Generate a memorable password (lowercase only)
python password_generator.py -l 16 --no-uppercase --no-digits --no-symbols
```

## Security Notes

- All passwords are generated using Python's `random` module with `random.choice()` and `random.shuffle()`
- For cryptographically secure random numbers, consider using `secrets` module instead of `random`
- Always use strong, unique passwords for each account
- Consider using a password manager to store generated passwords

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

**Neel Patel** - [eng-neelpatel](https://github.com/eng-neelpatel)

## Acknowledgments

- Built with Python's standard library
- Inspired by the need for quick, secure password generation
