import React, { useEffect, useState } from "react";

function News() {
  const [news, setNews] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Detect if running inside Docker container or in browser
    const API_URL =
      window.location.hostname === "localhost"
        ? "http://localhost:5000/api/news" // for browser access
        : "http://flask-backend:5000/api/news"; // for Docker internal calls

    fetch(API_URL)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => setNews(data))
      .catch((error) => {
        console.error("Error fetching news:", error);
        setError("Failed to fetch news");
      });
  }, []);

  return (
    <div>
     
      {error && <p style={{ color: "red" }}>{error}</p>}
      <ul>
        {news.map((item, index) => (
          <li key={index}>
            <a href={item.url} target="_blank" rel="noopener noreferrer">
              {item.title}
            </a>
            <p>{item.content}</p>
            <small>
              {item.publishedAt} - {item.source}
            </small>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default News;

