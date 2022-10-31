CREATE TABLE IF NOT EXISTS students (
  id INTEGER PRIMARY KEY,
  name TEXT,
  gender TEXT
);

INSERT OR IGNORE INTO `students` (`id`, `name`, `gender`)
VALUES
    (0001, '長岡 一馬', 'm'),
    (0002, '中本 知佳', 'f'),
    (0003, '松本 義文', 'm'),
    (0004, '佐竹 友香', 'f');

CREATE TABLE IF NOT EXISTS results (
  student_id INTEGER,
  subject TEXT,
  score INTEGER
);

INSERT OR IGNORE INTO `results` (`student_id`, `subject`, `score`)
VALUES
    (0001, '国語', 30),
    (0001, '英語', 30),
    (0002, '国語', 70),
    (0002, '数学', 80),
    (0003, '理科', 92),
    (0004, '社会', 90),
    (0004, '理科', 35),
    (0004, '英語', 22);
