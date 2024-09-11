use iced::pure::{button, column, row, text, Element, Sandbox};
use iced::{Alignment, Length, Settings};
use core::num;
use std::process;
#[derive(Default)]
struct Calculator {
    display_value: String,  // The value displayed in the dialog box (shown to the user)
    number_1: f64,          // The first number entered (before the operation)
    number_2: Option<f64>,  // The second number (entered after the operation)
    operation: Option<char>,// The selected operation (e.g., +, -, *, /)
}
#[derive(Debug, Clone)]
enum Message {
    InputNumber(char),   // For numeric inputs (characters like '1', '2', '3', etc.)
    Operation(char),     // For operations (+, -, *, /)
    Clear,               // Clear the inputs (reset the calculator)
    Equals,              // Calculate the result when "=" is pressed
    Exit,                // Exit the program (when 'X' is pressed)
}
impl Sandbox for Calculator {
    type Message = Message;

    // Initializes the Calculator application with default values
    fn new() -> Self {
        Calculator {
            display_value: "0".to_string(),  // Start by displaying "0"
            ..Default::default()  // Default values for number_1, number_2, and operation
        }
    }

    // The title of the application window
    fn title(&self) -> String {
        String::from("Rizz Calculator")
    }

    // Handles updates to the state of the application based on user actions
    fn update(&mut self, message: Message) {
        match message {
            Message::InputNumber(digit) => {
                // Handle the input of numbers (0-9)
                if self.display_value == "0" {
                    // If the current display is "0", replace it with the new digit
                    self.display_value = digit.to_string();
                } else {
                    // Otherwise, append the digit to the existing display value
                    self.display_value.push(digit);
                }
            }
            Message::Operation(op) => {
                // Handle operation selection (+, -, *, /)
                // Store number_1 and prepare to accept number_2 by clearing the display
                self.number_1 = self.display_value.parse().unwrap_or(0.0); // Parse and store number_1
                self.operation = Some(op);  // Store the operation (e.g., +, -, *, /)
                self.display_value = "0".to_string();  // Clear the display for number_2 input
            }
            Message::Clear => {
                self.display_value = "0".to_string();
                self.number_1 = 0.0;
                self.number_2 = None
            }
            Message::Equals => {
                // Handle the "=" operation (calculate the result)
                if let Some(op) = self.operation {
                    // Store the second number (number_2) from the current display
                    self.number_2 = Some(self.display_value.parse().unwrap_or(0.0));
                    if let Some(num2) = self.number_2 {
                        // Perform the calculation based on the selected operation
                        let result = match op {
                            '+' => self.number_1 + num2,
                            '-' => self.number_1 - num2,
                            '*' => self.number_1 * num2,
                            '/' => self.number_1 / num2,
                            _   => unreachable!()
                        };
                        self.display_value = result.to_string();
                        self.number_1 = result;
                        // Your code here
                        // Reset number_2 and the operation for further calculations
                        self.number_2 = None;
                        self.operation = None;
                    }
                }
            }
            Message::Exit => {
                // Exit the program when 'X' is pressed
                process::exit(0);
            }
        }
    }

    // Defines the layout and visual structure of the application
    fn view(&self) -> Element<Message> {
        // Display box to show the current value or result
        let display = text(&self.display_value)
            .size(50)  // Set font size for better readability
            .width(Length::Fill)  // Make it fill the available width
            .horizontal_alignment(iced::alignment::Horizontal::Center);  // Center the text

        // Helper function to create buttons with uniform style
        let button = |label: &str, msg: Message| {
            button(text(label))
                .on_press(msg)          // Trigger the corresponding message when pressed
                .padding(10)            // Add padding for button sizing
                .width(Length::Units(60))// Set a fixed width for buttons
        };

        // Layout for numeric buttons (0-9)
        let numbers = column()
            .push(
                row()  // Row for numbers 7, 8, 9
                    .push(button("7", Message::InputNumber('7')))
                    .push(button("8", Message::InputNumber('8')))
                    .push(button("9", Message::InputNumber('9')))
                    .spacing(10),  // Space between the buttons
            )
            .push(
                row()  // Row for numbers 4, 5, 6
                .push(button("4", Message::InputNumber('4')))
                .push(button("5", Message::InputNumber('5')))
                .push(button("6", Message::InputNumber('6')))
                .spacing(10),  // Space between the buttons                    .spacing(10),
            )
            .push(
                row()  // Row for numbers 1, 2, 3
                .push(button("1", Message::InputNumber('1')))
                .push(button("2", Message::InputNumber('2')))
                .push(button("3", Message::InputNumber('3')))
                .spacing(10),  // Space between the buttons                    .spacing(10),
            )
            .push(
                row()  // Row for number 0
                    .push(button("0", Message::InputNumber('0')))
            )
            .spacing(10);  // Spacing between rows

        // Layout for operation buttons and control buttons (C, =, X)
        let operations = column()
            .push(
                row()  // Row for operations +, -, *, /
                .push(button("+", Message::Operation('+')))
                .push(button("-", Message::Operation('-')))
                .push(button("*", Message::Operation('*')))
                .push(button("/", Message::Operation('/')))
                .spacing(10)
            )
            .spacing(10)
            .push(
                row()  // Row for control buttons C, =, X
                .push(button("C", Message::Clear))
                .push(button("=", Message::Equals))
                .push(button("Quit", Message::Exit)) 
                .spacing(10)          
            );

        // Combine the display, numeric buttons, and operation buttons into a single layout
        let content = column()
            .push(display)    // Add the display at the top
            .push(numbers)    // Add numeric buttons in the middle
            .push(operations) // Add operation and control buttons at the bottom
            .align_items(Alignment::Center)  // Center align all content
            .spacing(20);  // Space between the elements

        // Return the complete layout as an Element
        content.into()
    }
}

fn main() {
    // Run the Calculator application with default settings
    Calculator::run(Settings::default());
}

