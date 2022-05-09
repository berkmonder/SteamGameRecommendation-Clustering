def prediction(title, cs):
    game_id = df[df.Title == title].index[0]
    
    scores = list(enumerate(cs[game_id]))
    
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    sorted_scores = sorted_scores[1:]
    
    top=10
    recommendation=[]
    for item in sorted_scores[:top]:
        game_title = df.loc[df.index == item[0], ['gameId', 'Title', 'Review']].values[0]
        recommendation.append(game_title)
    
    return recommendation