class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        return sum(
            locals().get("a", 0) * (a := b) if (b := row.count("1")) else 0
            for row in bank
        )
