class Solution:
    
    def encode(self, strs: List[str]) -> str:
        strings = []
        for string in strs:
            strings.extend([str(len(string)), "#", string])
        return ''.join(strings)

    def decode(self, s: str) -> List[str]:
        left = 0
        index = 0
        strings = []
        while index < len(s):
            if s[index] == '#':
                length = int(s[left:index])
                if length > 0:
                    strings.append(s[index + 1: index + 1 + length])
                else:
                    strings.append("")
                index += (1 + length)
                left = index
            else: index += 1
        return strings