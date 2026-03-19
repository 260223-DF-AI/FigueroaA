from .starter_code.analysis import load_data

def main():
    filename = 'orders.csv'
    print("Working")
    try:
        load_data('DataAnalysis/starter_code/' + filename)
    except FileNotFoundError as e:
        print(e)
        
    word = ["words", "that", "I", "need"]

    print([(i, j) for i, j in word])
    

if __name__ == "__main__":
    main()