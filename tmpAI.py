"""
AI   ---- Black
User ---- White
"""
max_depth = 2
L = 15
max_grid_cnt = L * L
max_score = 9999999999
priority_seq = [i for i in range(100)]
# define the "board situation" = Black_score - White_score

def H(black, white):
  global max_grid_cnt, max_score

  visited = [ [False for i in range(4)] for j in range(L*L) ]
  
  def search(pos, direction, is_Black):
    # search in the given direction
    if is_Black:
      this = black
      that = white
    else:
      this = white
      that = black
    x1 = pos
    x2 = pos
    if direction == 0:
      # vertical
      while x1 >= 0 and x1 in this: 
        x1 -= L
        visited[x1][direction] = True
      y1 = x1
      if x1 >= 0:
        while x1 >= 0 and x1 not in that:
          x1 -= L

      while x2 < max_grid_cnt and x2 in this: 
        x2 += L
        visited[x2][direction] = True
      y2 = x2
      if x2 < max_grid_cnt:
        while x2 < max_grid_cnt and x2 not in that:
          x2 += L
      left_empty = ( y1 - x1 ) / L
      right_empty = ( x2 - y2 ) / L
      contin_cnt = (y2 - y1 - L - L) / L

    elif direction == 1:
      # horizontal
      while x1 >= 0 and x1 in this: 
        x1 -= 1
        visited[x1][direction] = True
      y1 = x1
      if x1 >= 0:
        while x1 >= 0 and x1 not in that:
          x1 -= 1

      while x2 < max_grid_cnt and x2 in this: 
        x2 += 1
        visited[x2][direction] = True
      y2 = x2
      if x2 < max_grid_cnt:
        while x2 < max_grid_cnt and x2 not in that:
          x2 += 1
      left_empty = y1 - x1
      right_empty = x2 - y2
      contin_cnt = y2 - y1 - 2
    
    elif direction == 2:
      # left up -- right down '\'
      while x1 >= 0 and x1 in this: 
        x1 -= L + 1
        visited[x1][direction] = True
        if (x1 + L + 1) % L == 0:
          break
      y1 = x1
      if x1 >= 0:
        while x1 >= 0 and x1 not in that:
          x1 -= L + 1
          if (x1 + L + 1) % L == 0:
            break

      while x2 < max_grid_cnt and x2 in this:
        x2 += L + 1
        visited[x2][direction] = True
        if (x2 - L - 1) % L == (L - 1):
          break
      y2 = x2
      if x2 < max_grid_cnt:
        while x2 < max_grid_cnt and x2 not in that:
          x2 += L + 1
          if (x2 - L - 1 ) % L == (L - 1):
            break
      left_empty = ( y1 - x1 ) / (L + 1)
      right_empty = ( x2 - y2 ) / (L + 1)
      contin_cnt = (y2 - y1 - L - L -2 ) / (L + 1)

    else:
      # left down -- right up '/'
      while x1 >= 0 and x1 in this: 
        x1 -= L - 1
        visited[x1][direction] = True
        if (x1 + L - 1) % L == (L - 1):
          break
      y1 = x1
      if x1 >= 0:
        while x1 >= 0 and x1 not in that:
          x1 -= L - 1
          if (x1 + L - 1) % L == (L - 1):
            break

      while x2 < max_grid_cnt and x2 in this: 
        x2 += L - 1
        visited[x2][direction] = True
        if (x2 - L + 1) % L == 0:
          break
      y2 = x2
      if x2 < max_grid_cnt:
        while x2 < max_grid_cnt and x2 not in that:
          x2 += L - 1
          if (x2 - L + 1) % L == 0:
            break
      left_empty = ( y1 - x1 ) / (L - 1)
      right_empty = ( x2 - y2 ) / (L - 1)
      contin_cnt = (y2 - y1 - L - L + 2) / (L - 1)

    # calculate the SCORE!
    if contin_cnt >= 5 or (contin_cnt == 4 and (left_empty or right_empty)): 
      return max_score
    return contin_cnt * min(10, left_empty + contin_cnt + right_empty)


  def get_score(chess_list, is_Black):
    score = 0
    for pos in chess_list:
      # calulate the score of the color given
      for direction in range(4):
        if not visited[pos][direction]:
          visited[pos][direction] = True
          score += search(pos, direction, is_Black)
    return score
  
  black_score = get_score(black, True)
  white_score = get_score(white, False)

  return black_score - white_score

def dfs(black, white, depth):
  global max_depth
  ############
  'alpha-beta cutting'
  ############

  if depth >= max_depth:
    return (-1, H(black, white))

  elif depth % 2 == 0:
    # AI play. max-level
    choice = -1
    max_score = -99999999
    for i in priority_seq:
      if i not in black and i not in white:
        (pos, score) = dfs( black + [i], white, depth + 1 )
        if score > max_score:
          max_score = score
          choice = i
    return (choice, max_score) 
        
  else:
    # user play. min-level
    choice = -1
    min_score = 99999999
    for i in priority_seq:
      if i not in black and i not in white:
        (pos, score) = dfs( black, white + [i], depth + 1 )
        if score < min_score:
          min_score = score
          choice = i
    return (choice, min_score) 


def play(white, black):
  # return the position AI place black chess.
  (pos, score) = dfs(white, black, 0) 
  return pos
