results = {}  # user, points
submissions = {}  # lang, users count
banned_users = []

while True:
    command = input()
    if command == 'exam finished':
        break

    if 'banned' in command:
        tokens = command.split('-')
        user = tokens[0]
        banned_users.append(user)
        continue

    user, lang, points = command.split('-', maxsplit=2)
    if user not in results:
        results[user] = int(points)
    else:
        if int(points) > results[user]:
            results[user] = int(points)

    if lang not in submissions:
        submissions[lang] = [user]
    else:
        submissions[lang].append(user)

for user in banned_users:
    if user in results:
        del results[user]

ordered_results = dict(sorted(results.items(), key=lambda el: (-el[1], el[0])))
ordered_submissions = dict(sorted(submissions.items(), key=lambda el: (-len(el[1]), el[0])))
print('Results:')
[print(f'{user} | {points}') for user, points in ordered_results.items()]
print('Submissions:')
[print(f'{lang} - {len(submissions[lang])}') for lang in ordered_submissions]

