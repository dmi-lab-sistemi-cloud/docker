# Esempio di containerizzazione di un'applicazione Java Spring Boot

- Per mandare in esecuzione l'applicazione: `docker compose up`
- Per mandare in esecuzione l'applicazione forzando il rebuild di un'immagine già creata: `docker compose up --build` 
- Per arrestare l'applicazione: `docker compose down`
- Per arrestare l'applicazione e cancellare anche i volumi: `docker compose down --volumes`
- Per verificare il corretto funzionamento: `curl localhost:5000` restituisce "Hello from Red Planet"