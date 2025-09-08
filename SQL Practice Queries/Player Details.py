SELECT m.match_id,
       m.player_1,
       m.player_2,
       m.winner,
       m.match_date,
       p.score
FROM Matches m
JOIN Players p
  ON p.player_name = m.winner
ORDER BY m.match_date DESC, m.match_id DESC
LIMIT 5;
