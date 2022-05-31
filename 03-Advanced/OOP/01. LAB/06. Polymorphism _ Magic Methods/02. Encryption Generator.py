class EncryptionGenerator:
    def __init__(self, text: str):
        self.text = text

    def __add__(self, n):
        if not isinstance(n, int):
            raise ValueError("You must add a number.")
        new_text = ''
        for ch in self.text:
            # implement range 32 : 126
            new_num = ord(ch) + n
            if new_num < 32:
                residue = 32 - new_num
                new_num = 127 - residue
            elif new_num > 126:
                residue = new_num - 126
                new_num = 31 + residue
            new_text += chr(new_num)
        return new_text


example = EncryptionGenerator('Super-Secret Message')
print(example + 20)
print(example + (-52))