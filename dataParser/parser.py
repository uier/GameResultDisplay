import csv
import json

def read_csv(file_name):
	with open(file_name) as f:
		c = list(csv.reader(f))
	return c

def parse_csv(csv_file):
	p = list(map(lambda d: d[1:], csv_file[2:]))
	p = [[0] * 7] + [map(lambda u: (lambda x: x//100*60 + x%100)(int(u)) if u else 0, v) for i, v in enumerate(p) if (i - 1)%4 and (i - 2)%4]
	p = map(lambda q: q[:q.index(0, 1)] + q[-2:], zip(*p))
	p = map(lambda q: [*map(lambda team, stime, etime: [team, etime - stime], q[0::2], q[1::2], q[3::2])], p)
	p = map(lambda q: q[:-1] + [[q[-1][0], max(q[-1][1], 5)]], p)
	p = [[r[0] for r in q for i in range(r[1])] for q in p]
	p = (lambda l: map(lambda q: q + [0]*(l - len(q)), p))(max(map(len, p)))

	return json.dumps([*p])

if __name__ == '__main__':
	csv_file = read_csv('scoreboard.csv')
	json_file = parse_csv(csv_file)
	print(json_file)
