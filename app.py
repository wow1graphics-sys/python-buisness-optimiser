
# Corporate Budget & Profit Margin Optimizer
# Developed by a future Software Engineer blending Business + Tech logic

def calculate_business_metrics():
    print("=" * 50)
    print("      CORPORATE BUDGET & MARGIN OPTIMIZER       ")
    print("=" * 50)
    
    try:
        product_name = input("Enter your product or service name: ")
        selling_price = float(input(f"Enter selling price per unit of {product_name} ($): "))
        variable_cost = float(input("Enter variable cost per unit (materials, labor) ($): "))
        fixed_costs = float(input("Enter total monthly fixed costs (rent, salaries, marketing) ($): "))
        expected_sales = int(input("Enter expected monthly units sold: "))
    except ValueError:
        print("\n[Error] Please enter valid numbers for prices, costs, and sales numbers.")
        return

    total_revenue = selling_price * expected_sales
    total_variable_cost = variable_cost * expected_sales
    total_costs = fixed_costs + total_variable_cost
    
    net_profit = total_revenue - total_costs
    
    if total_revenue > 0:
        profit_margin_percentage = (net_profit / total_revenue) * 100
    else:
        profit_margin_percentage = 0.0

    contribution_margin = selling_price - variable_cost
    if contribution_margin > 0:
        break_even_units = fixed_costs / contribution_margin
    else:
        break_even_units = float('inf')

    print("\n" + "-" * 50)
    print(f" FINANCIAL PERFORMANCE REPORT FOR: {product_name.upper()} ")
    print("-" * 50)
    print(f"💰 Total Monthly Revenue:     ${total_revenue:,.2f}")
    print(f"📉 Total Monthly Expenses:    ${total_costs:,.2f}")
    print(f"🟩 Net Monthly Profit:        ${net_profit:,.2f}")
    print(f"📊 Net Profit Margin:         {profit_margin_percentage:.2f}%")
    print("-" * 50)
    
    if net_profit > 0:
        print(f"✅ STATUS: PROFITABLE. You clear your break-even line of {int(break_even_units)} units.")
    elif net_profit == 0:
        print(f"⚠️ STATUS: BREAK-EVEN. Operating exactly at cost.")
    else:
        print(f"❌ STATUS: LOSS-MAKING. You need to sell {int(break_even_units) - expected_sales} more units to break even.")
    print("=" * 50)

if _name_ == "_main_":
    calculate_business_metrics(
