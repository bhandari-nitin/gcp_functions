from flask import Flask, request

def main(request):
	data = request.get_json()
	return data
