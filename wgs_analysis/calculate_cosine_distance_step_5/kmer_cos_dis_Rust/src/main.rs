#[allow(dead_code)]
#[allow(unused_variables)]


use std::io::{self, Read};
use std::fs::File;
use std::env;

mod numeric;
use numeric::cosine;


 //q how to silence "unused function warning"?

fn filename_to_string(s: &str) -> io::Result<String> {
    let mut file = File::open(s)?;
    let mut s = String::new();
    file.read_to_string(&mut s)?;
    Ok(s)
}

fn words_by_line<'a>(s: &'a str) -> Vec<Vec<&'a str>> {
    s.lines().map(|line| {
        line.split_whitespace().collect()
    }).collect()
}

fn main() {
    

    let args: Vec<String> = env::args().collect();
    let input_kmer_freq_file = &args[1];
    // println!("In file {}", input_kmer_freq_file);

    let whole_file = filename_to_string(input_kmer_freq_file).unwrap();
    let frequencies = words_by_line(&whole_file);

    let mut x_vec_test: Vec<f64> = vec![];
    let mut y_vec_test: Vec<f64> = vec![];

    //make sure the vector is of same size as file length or dont define length of vector at all

    for x in frequencies.iter() {
        x_vec_test.push(x[0].parse().unwrap());
        y_vec_test.push(x[1].parse().unwrap());

    }

    let cos_sim: f64 = cosine(&x_vec_test,&y_vec_test);
    //println!("{}", cos_sim);
    //println!("{}", 1.0 - cos_sim);

    println!("{} {} {}", input_kmer_freq_file, cos_sim, 1.0 - cos_sim)

}

