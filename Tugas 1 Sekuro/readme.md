1. class Genshin
    - probability: berisi probabilitas untuk setiap rarity item yang tersedia
        5 star: Paling rare, dengan probabilitas 0.6% per pull
        4 star: Tidak begitu rare, dengan probabilitas 5.1% per pull
        3 star: tidak rare, dengan probabilitas 94.3% per pull
    - pools: kumpulan item berdasarkan rarity yang nantinya akan dipilih secara acak berdasarkan probabilitas
    - pity_5_star dan pity_4_star: Hitungan pity untuk 5 star dan 4 star
    - primogem: Melacak jumlah primogem yang tersedia

    pity adalah mekanisme yang menjamin untuk mendapatkan item dengan probability dan rarity tertentu setelah sejumlah pull yang tidak memberikan item tersebut
    primogem adalah currency yaang digunakan untuk gatcha
    increase_pity() = Menambah hitungan pity.
    reset_pity_4_star() = Mereset hitungan pity 4 star.
    reset_pity_5_star() = Mereset hitungan pity 5 star.

2. class Gatcha
    - untuk mengatur sistem gatcha, sepert pemeriksaan pity dan menentukan item secara random yang didapatkan berdasarkan probabilitas untuk setiap rarity
    - Jika pity_5_star sudah mencapai 90 tanpa mendapatkan item 5-star, maka akan secara otomatis mendapatkan item 5 star secara random
    - Jika pity_4_star sudah mencapai 10 pull tanpa mendapatkan item 4-star, maka akan secara otomatis mendapatkan item 4 star secara random. Setelah itu, pity_4_star di reset ke 0 dan pity_5_star akan meningkat 1.

    program akan menentukan nilai pull secara acak dari 0 - 100
    - Jika nilai acak pull pada batas probability 5 star, maka akan mendapatkan item 5 star secara random.
    - Jika nilai acak pull pada batas probability 4 star, maka akan mendapatkan item 4 star secara random.
    - Jika tidak memenuhi kedua kriteria tersebut, maka akan mendapatkan item 3 star secara random

3. class Pull
    - Mengelola proses gatcha dengan 10-pull setiap memulai dan menanyakan apakah mereka ingin melakukan 10 pull lagi atau tidak
    - Setelah melakukan 10 pull akan ditanyakan lagi apakah ingin melakukan 10 pull lagi. Jika yes dan primogem cukup, maka melakukan 10 pull lagi 
    - Setiap 10 pull mengurangi akan mengurangi 1600 primogem. Jika primogem tidak cukup, maka program berhenti.