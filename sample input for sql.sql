create database social_media_app_zubi;
use social_media_app_zubi;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    bio TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

INSERT INTO users (username, email, password_hash, full_name, bio, is_private) 
VALUES (
    'zubi', 
    'zuhaiblotus@gmail.com', 
    SHA2('9811', 256), 
    'Zuhaib Kamal', 
    'bomb bio'
);

INSERT INTO users (username, email, password_hash, full_name, bio, is_private) 
VALUES (
    'sahil', 
    'sahil@gmail.com', 
    SHA2('9811', 256), 
    'sahil', 
    'bomb bio'
);
CREATE TABLE follows (
    follow_id INT AUTO_INCREMENT PRIMARY KEY,
    follower_id INT NOT NULL,
    followed_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (follower_id) REFERENCES users(user_id),
    FOREIGN KEY (followed_id) REFERENCES users(user_id)
);

INSERT INTO follows (follower_id, followed_id) 
VALUES (2, 1);

CREATE TABLE posts (
    post_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    content TEXT NOT NULL,
    visibility ENUM('public', 'followers only', 'private') NOT NULL DEFAULT 'public',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO posts (user_id, content, visibility) 
VALUES (1, 'This is a test.', 'public');

INSERT INTO posts (user_id, content, visibility) 
VALUES (1, 'This is a test.', 'followers only');


