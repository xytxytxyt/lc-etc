# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

def climbingLeaderboard(ranked, player):
    ranked_seen = set()
    ranked_distinct = []
    for r in ranked:
        if r not in ranked_seen:
            ranked_distinct.append(r)
        ranked_seen.add(r)
    ranked = ranked_distinct
    i = len(ranked) - 1
    j = 0
    ranks = []
    while i >= 0 and j < len(player):
        # print(i, j, ranked, player, ranks)
        if ranked[i] > player[j]:
            ranks.append(i + 2)
            j += 1
        elif ranked[i] == player[j]:
            ranks.append(i + 1)
            j += 1
        else:
            i -= 1
    ranks += [1 for k in range(len(player) - j)]
    return ranks


if __name__ == "__main__":
    from test0 import ranked, player, answer
    # print(ranked)
    # print(player)
    output = climbingLeaderboard(ranked, player)
    assert output == answer, f"correct answer:\n{answer}\noutput:\n{output}"
