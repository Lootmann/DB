import sqlite3 from "sqlite3";

const db = new sqlite3.Database(":memory:");

db.serialize(() => {
  // run
  db.run("CREATE TABLE IF NOT EXISTS test (info TEXT)");

  // prepare to run
  const stmt = db.prepare("INSERT INTO test VALUES (?)");

  for (let i = 0; i < 10; ++i) {
    // prepare run
    stmt.run(`Hello ${i}`);
  }

  stmt.finalize();

  // get run
  db.each("SELECT rowid AS id, info FROM test", (err, row) => {
    console.log(row.id + ": " + row.info);
  });
});

db.close();
