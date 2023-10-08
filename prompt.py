from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import psycopg2
import pandas as pd
import numpy as np



# load database login info
df = pd.read_csv('credentials.csv')
credentials = np.array(df)[:]

DB_NAME = credentials[0][0]
DB_USER = credentials[0][1]
DB_PASS = credentials[0][2]
DB_HOST = credentials[0][3]
DB_PORT = credentials[0][4]




# FastAPI app
app = FastAPI()

# Homepage
@app.get('/')
async def root():
	return {'greeting': 'Welcome to Promptly!'}

# A & B prompts
@app.get('/a_b')
async def a_b():
	# connect to db and open cursor
	conn = psycopg2.connect(database=DB_NAME
				, user=DB_USER
				, password=DB_PASS
				, host=DB_HOST
				, port=DB_PORT)
	cur = conn.cursor()

	# grab random prompt
	cur.execute(
		'SELECT * FROM a_b ORDER BY RANDOM() LIMIT 1;'
		)
	prompt = cur.fetchone()
	prompt = prompt[1]
	print('a_b prompt: ' + prompt)

	# close connections
	cur.close()
	conn.close()

	return {prompt}


# A & B & C prompts
@app.get('/a_b_c')
async def a_b_c():
	# connect to db and open cursor
	conn = psycopg2.connect(database=DB_NAME
				, user=DB_USER
				, password=DB_PASS
				, host=DB_HOST
				, port=DB_PORT)
	cur = conn.cursor()

	# grab random prompt
	cur.execute(
		'SELECT * FROM a_b_c ORDER BY RANDOM() LIMIT 1;'
		)
	prompt = cur.fetchone()
	prompt = prompt[1]
	print('a_b_c prompt: ' + prompt)

	# close connections
	cur.close()
	conn.close()

	return {prompt}


# dialogue prompts
@app.get('/dialogue')
async def dialogue():
	# connect to database
	conn = psycopg2.connect(database=DB_NAME
				, user=DB_USER
				, password=DB_PASS
				, host=DB_HOST
				, port=DB_PORT)

	# open cursor to perform database operations
	cur = conn.cursor()

	# grab random dialogue prompt
	cur.execute(
		'SELECT * FROM dialogue ORDER BY RANDOM() LIMIT 1;'
		)
	prompt = cur.fetchone()
	prompt = prompt[1]
	print('Dialogue prompt: ' + prompt)

	# close communication with database
	cur.close()
	conn.close()

	return {prompt}


# drawing prompts
@app.get('/drawing')
async def drawing():
	# connect to db and open cursor
	conn = psycopg2.connect(database=DB_NAME
				, user=DB_USER
				, password=DB_PASS
				, host=DB_HOST
				, port=DB_PORT)
	cur = conn.cursor()

	# grab random prompt
	cur.execute(
		'SELECT * FROM drawing ORDER BY RANDOM() LIMIT 1;'
		)
	prompt = cur.fetchone()
	prompt = prompt[1]
	print('drawing prompt: ' + prompt)

	# close connections
	cur.close()
	conn.close()

	return {prompt}


# nsfw prompts
@app.get('/nsfw')
async def nsfw():
	# connect to db and open cursor
	conn = psycopg2.connect(database=DB_NAME
				, user=DB_USER
				, password=DB_PASS
				, host=DB_HOST
				, port=DB_PORT)
	cur = conn.cursor()

	# grab random prompt
	cur.execute(
		'SELECT * FROM nsfw ORDER BY RANDOM() LIMIT 1;'
		)
	prompt = cur.fetchone()
	prompt = prompt[1]
	print('nsfw prompt: ' + prompt)

	# close connections
	cur.close()
	conn.close()

	return {prompt}


# prose prompts
@app.get('/prose')
async def prose():
	# connect to db and open cursor
	conn = psycopg2.connect(database=DB_NAME
				, user=DB_USER
				, password=DB_PASS
				, host=DB_HOST
				, port=DB_PORT)
	cur = conn.cursor()

	# grab random prompt
	cur.execute(
		'SELECT * FROM prose ORDER BY RANDOM() LIMIT 1;'
		)
	prompt = cur.fetchone()
	prompt = prompt[1]
	print('prose prompt: ' + prompt)

	# close connections
	cur.close()
	conn.close()

	return {prompt}


# scenario prompts
@app.get('/scenario')
async def scenario():
	# connect to db and open cursor
	conn = psycopg2.connect(database=DB_NAME
				, user=DB_USER
				, password=DB_PASS
				, host=DB_HOST
				, port=DB_PORT)
	cur = conn.cursor()

	# grab random prompt
	cur.execute(
		'SELECT * FROM scenario ORDER BY RANDOM() LIMIT 1;'
		)
	prompt = cur.fetchone()
	prompt = prompt[1]
	print('scenario prompt: ' + prompt)

	# close connections
	cur.close()
	conn.close()

	return {prompt}



if __name__ == '__main__':
	run(app='dialgue:app', reload=True, host='192.168.1.18', port=8000)

