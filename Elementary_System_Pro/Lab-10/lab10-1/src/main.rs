use iced::Settings;
use iced::pure::widget::{Button, Column, Container, Text, Row};
use iced::pure::Sandbox;
use iced::{Length, Alignment};
use std::process;

fn main() -> Result<(), iced::Error> {
    // Set custom window size in the Settings
    let settings = Settings {
        window: iced::window::Settings {
            size: (400, 300),  // Set window size to 400x300
            resizable: true,    // Allow window to be resizable
            ..Default::default()
        },
        ..Default::default()
    };

    Counter::run(settings)
}

struct Counter {
    count: i32,
}

#[derive(Debug, Clone, Copy)]
enum CounterMessage {
    Increment,
    Decrement,
    Clear,
    Exit,
}

impl Sandbox for Counter {
    type Message = CounterMessage;

    fn new() -> Self {
        Counter { count: 0 }
    }

    fn title(&self) -> String {
        String::from("Counter app")
    }

    fn update(&mut self, message: Self::Message) {
        match message {
            CounterMessage::Increment => self.count += 1,
            CounterMessage::Decrement => self.count -= 1,
            CounterMessage::Clear => self.count = 0,
            CounterMessage::Exit => process::exit(0),  // Exit the program
        }
    }

    fn view(&self) -> iced::pure::Element<Self::Message> {
        let label = Text::new(format!("Count: {}", self.count))
            .size(30);  // Set text size

        let incr = Button::new("INC")
            .padding(10)  // Add padding to buttons
            .on_press(CounterMessage::Increment);
            
        let decr = Button::new("DEC")
            .padding(10)
            .on_press(CounterMessage::Decrement);

        let exit = Button::new("EXIT")
            .padding(10)
            .on_press(CounterMessage::Exit);  // Button to exit program

        // Create a Row to align INC, Count, and DEC horizontally
        let button_row = Row::new()
            .push(incr)
            .push(label)
            .push(decr)
            .spacing(20)  // Add spacing between buttons
            .align_items(Alignment::Center);  // Center them vertically

        // Create a Column to align the row and the exit button
        let layout = Column::new()
            .push(button_row)  // Add the row with INC, Count, and DEC
            .push(exit)        // Add the EXIT button below the row
            .spacing(20)       // Add spacing between the row and the EXIT button
            .align_items(Alignment::Center);  // Center elements horizontally

        Container::new(layout)
            .center_x()
            .center_y()
            .width(Length::Fill)
            .height(Length::Fill)
            .into()
    }
}
