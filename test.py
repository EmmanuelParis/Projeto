movieDuration = input('\033[34mDigite a duração do filme em minutos: \033[m')  
movieHour = int(movieDuration) // 60
movieMinutes = int(movieDuration) % 60
                            








movieTime = input(f'\033[34mDigite o horário que o filme vai passar na {'a'} [HH:MM]: \033[m')
if len(movieTime) == 5 and movieTime[2] == ':':
    movieTime = movieTime[:2] + movieTime[3:]

























ratingTomato = movieDuration[0] + movieTime[1] + '%'

print(ratingTomato)