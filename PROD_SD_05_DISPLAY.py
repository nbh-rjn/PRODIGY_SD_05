import tkinter as tk
import csv


def load_data(csv_filename):
    data = []
    with open(csv_filename, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            data.append(dict(zip(header, row)))
    return data


def create_widgets(root, data, current_row_var):
    name_label = tk.Label(root, text="Name:", font=("Consolas", 12), bg='#4B416F', fg='white')
    name_label.grid(row=2, column=0, padx=10, pady=10)

    price_label = tk.Label(root, text="Price:", font=("Consolas", 12), bg='#4B416F', fg='white')
    price_label.grid(row=3, column=0, padx=10, pady=10)

    info_label = tk.Label(root, text="Information:", font=("Consolas", 12), bg='#4B416F', fg='white')
    info_label.grid(row=4, column=0, padx=10, pady=10)

    availability_label = tk.Label(root, text="Availability:", font=("Consolas", 12), bg='#4B416F', fg='white')
    availability_label.grid(row=5, column=0, padx=10, pady=10)

    next_button = tk.Button(root, text="Next",
                            command=lambda: show_next_row(data, current_row_var, name_label, price_label, info_label, availability_label),
                            font=('Consolas', 12))

    next_button.grid(row=6, column=0, padx=10, pady=10, sticky='w')

    # Display the first row
    show_row(data, current_row_var, name_label, price_label, info_label, availability_label)


def show_row(data, current_row_var, name_label, price_label, info_label, availability_label):
    current_row = current_row_var.get()
    if 0 <= current_row < len(data):
        row_data = data[current_row]
        name_label.config(text=f"Name: {row_data['Name']}", anchor='w', font=("Consolas", 10))
        price_label.config(text=f"Price: {row_data['Price']}", anchor='w', font=("Consolas", 10))

        information_text = '\n'.join(row_data['Information'].split(','))
        info_label.config(text=f"Information:\n {information_text}", anchor='w', font=("Consolas", 10))
        availability_label.config(text=f"Availability: {row_data['Availability']}", anchor='w', font=("Consolas", 10))
    else:
        # Reset labels if there is no more data
        name_label.config(text="Name:")
        price_label.config(text="Price:")
        info_label.config(text="Information:")
        availability_label.config(text="Availability:")


def show_next_row(data, current_row_var, name_label, price_label, info_label, availability_label):
    current_row_var.set(current_row_var.get() + 1)
    show_row(data, current_row_var, name_label, price_label, info_label, availability_label)


def main():
    root = tk.Tk()
    root.geometry("850x350")
    root.title("Web Scraper Display")

    background_image = tk.PhotoImage(file="task4_image.png")
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    label = tk.Label(root, text=f"Web Scraping E-Commerce Sites", bg='#2B0457', fg='white',
                     font=('Consolas', 16, 'bold'))
    label.grid(padx=10, pady=10, sticky='n')

    csv_filename = 'file.csv'
    data = load_data(csv_filename)

    current_row_var = tk.IntVar(value=0)
    create_widgets(root, data, current_row_var)

    root.mainloop()


if __name__ == "__main__":
    main()
