from flask import Flask

app = Flask(__name__)
balance = 0

@app.route('/<op>/<int:money>/')
def bank(op, money):
    global balance
    if op == 'deposit':
        balance += money
        return "<h2>입금 %d 원, 잔액 %d</h2>" % (money, balance)
    elif op == 'withdraw':
        withdraw = balance if balance < money else money
        balance -= withdraw
        return "<h2>출금 %d 원, 잔액 %d</h2>" % (withdraw, balance)
    else:
        return "deposit 또는 withdraw 중 하나를 입력하세요"

@app.route('/inquiry/')
def inquiry():
    return "<h2>잔액 %d </h2>" % (balance)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
