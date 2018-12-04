from flask import Flask, render_template, request, redirect
import data_manager

app = Flask(__name__)


@app.route("/")
def index():
    table_names = data_manager.get_table_names()
    table = data_manager.get_table_name(request.args.get('table_name'))
    order_by = data_manager.get_order_by(request.args.get('order_by'))
    order_direction = data_manager.get_order_direction(request.args.get('order_direction'))
    ordered_products = data_manager.get_ordered_products(table, order_by, order_direction)
    if request.args.get('search'):
        search = '%' + request.args.get('search') + '%'
        ordered_products = data_manager.get_searched_product_names(table, search)

    return render_template('index.html', ordered_products=ordered_products, order_by=order_by,
                           table_names=table_names)


if __name__ == "__main__":
    app.run(debug=False, port=5005)
