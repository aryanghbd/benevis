# Benevis
Benevis - A Persian programming language.

# About

Benevis is a programming language that allows you to write code in Persian. The compiler for Benevis is written in Python and uses the RPLY library for lexing and parsing. Support is implemented for both Latinised (Pinglish) Farsi and Perso-Arabic Farsi, with new features being added in regularly.

## Getting Started

To start using Benevis, you need to have Python installed on your system. Benevis works with Python 3.9+.

### Installation

To install Benevis, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/aryanghbd/benevis.git
    ```

2. Navigate into the cloned directory:
    ```bash
    cd benevis
    ```

3. Install the package:
    ```bash
    pip install .
    ```

### Usage

After installation, you can start Benevis with the following command:

```bash
benevis [filename]
```

Note that benevis files have the extension '.bnvs'.

If you require any help setting up, call
```bash
benevis -h
```

### Contributions

I am actively seeking to collaborate with fellow developers or linguists of the Persian language to really provide more expansive ranges of syntax for the language! If you're interested, contact me on LinkedIn or fork this project and drop me a message, let's try and put Farsi back on top!

### Finally, a motivation

Why did I make this project? I felt that the barrier to entry for a lot of young programmers can often scale with their level of spoken or written English, many among our youth have the arithmetic and logical capabilities to write code at an early age but are often hampered by a lack of intuition of said concepts in the English language, as often they are not taught the language at all or until far later in life. This leads to an increased difficulty of having to translate thoughts into English, and then subsequently into code. I made benevis to support the Persian-speaking youth, by providing a simple but expanding means of expressing code in a way that makes sense in their own language.
