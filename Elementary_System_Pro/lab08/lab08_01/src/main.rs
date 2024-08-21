use std::fs::{self, File};
use std::io::{self, BufRead, Write};
use std::path::Path;
use std::process::exit;
use std::ptr::NonNull;

fn main() {
    let mut file_name: Option<String> = None;  // Use Option to track if a file is open
    let mut file_content: Vec<String> = Vec::new();
    loop {
        println!("\nMenu:");
        println!("1. Open file");
        println!("2. Display content");
        println!("3. Add line");
        println!("4. Delete line");
        println!("5. Write file");
        println!("6. Exit");
        let mut first = "";
        let mut rest = "";
        let mut choice = String::new();
        io::stdin().read_line(&mut choice).expect("Failed to read line");
        let choice = choice.trim();
        match choice.split_once(' ') {
            Some(sth) => {
                (first,rest) = sth;
            }
            None => {
                first = choice;
            }
        }
        match first {
            "open" => {
                file_name = open_file(&mut file_content, rest);  // Update file_name
            }
            "display" => {
                if file_name.is_none() {
                    println!("No file open. Please open a file first.");
                } else {
                    display_content(&file_content);
                }
            }
            "add" => {
                if file_name.is_none() {
                    println!("No file open. Please open a file first.");
                } else {
                    add_line(&mut file_content , rest);
                }
            }
            "delete" => {
                if file_name.is_none() {
                    println!("No file open. Please open a file first.");
                } else {
                    delete_line(&mut file_content, rest);
                }
            }
            "write" => {
                if let Some(ref file) = file_name {
                    write_file(file, &file_content);
                } else {
                    println!("No file open. Please open a file first.");
                }
            }
            "exit" => {
                println!("Exiting...");
                exit(0);
            }
            _ => {
                println!("Invalid choice. Please select an option from the menu.");
            }
        }
    }
}

fn open_file(file_content: &mut Vec<String>, meow:&str) -> Option<String> {
    println!("Enter the file name to open:");
    let file_name = meow.trim().to_string();

    if Path::new(&file_name).exists() {
        let file = File::open(&file_name).expect("Unable to open file");
        let reader = io::BufReader::new(file);
        file_content.clear();
        for line in reader.lines() {
            file_content.push(line.expect("Unable to read line"));
        }
        println!("File opened successfully.");
        Some(file_name)  // Return the file name
    } else {
        println!("File does not exist. Do you want to create a new file? (y/n)");
        let mut create_new = String::new();
        io::stdin().read_line(&mut create_new).expect("Failed to read line");
        if create_new.trim().eq_ignore_ascii_case("y") {
            if meow.len() == 0{
                println!("Cannot create a file without a name.");
                return None
            }
            file_content.clear();
            println!("New file created. You can now add lines and save the file.");
            Some(file_name)  // Return the new file name
        } else {
            println!("File not opened.");
            None  // No file name, return None
        }
    }
}

fn display_content(file_content: &[String]) {
    if file_content.is_empty() {
        println!("File is empty.");
    } else {
        println!("File content:");
        for (index, line) in file_content.iter().enumerate() {
            println!("{}: {}", index + 1, line);
        }
    }
}

fn add_line(file_content: &mut Vec<String> , meow:&str) {
    println!("Enter the line to add:");
    let new_line = meow;
    file_content.push(new_line.trim().to_string());
    println!("Line added.");
}

fn delete_line(file_content: &mut Vec<String> , meow:&str) {
    display_content(file_content);
    println!("Enter the line number to delete:");
    let  line_number = meow;
    let line_number: usize = line_number.trim().parse().expect("Please enter a valid number");

    if line_number > 0 && line_number <= file_content.len() {
        file_content.remove(line_number - 1);
        println!("Line deleted.");
    } else {
        println!("Invalid line number.");
    }
}

fn write_file(file_name: &str, file_content: &[String]) {
    let mut file = File::create(file_name).expect("Unable to create file");
    for line in file_content {
        writeln!(file, "{}", line).expect("Unable to write line");
    }
    println!("File written successfully.");
}
