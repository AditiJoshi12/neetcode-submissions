class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        freq = {}
        n = len(hand)

        for i in range(n):
            freq[hand[i]] = freq.get(hand[i], 0) + 1

        for card in sorted(hand):
            count = freq[card]

            if count > 0:
                for i in range(0, groupSize):
                    if freq.get(card+i, 0) < count:
                        return False                    
                    freq[card+i] -= count

        return True
                    