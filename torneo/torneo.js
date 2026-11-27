const players = [
    { id: "nerea", name: "Nerea", blade: "Aero Sting" },
    { id: "marcos", name: "Marcos", blade: "Dran Sword" },
    { id: "lucia", name: "Lucía", blade: "Wizard Arrow" },
    { id: "adrian", name: "Adrián", blade: "Leon Claw" },
    { id: "sofia", name: "Sofía", blade: "Hell Scythe" },
    { id: "diego", name: "Diego", blade: "Shark Edge" },
    { id: "emma", name: "Emma", blade: "Knight Shield" },
    { id: "hugo", name: "Hugo", blade: "Viper Tail" }
];

const rounds = [
    {
        title: "RONDA 1 · CUARTOS",
        matches: [
            { id: "q1", label: "DUELO 01", players: [players[0], players[1]] },
            { id: "q2", label: "DUELO 02", players: [players[2], players[3]] },
            { id: "q3", label: "DUELO 03", players: [players[4], players[5]] },
            { id: "q4", label: "DUELO 04", players: [players[6], players[7]] }
        ]
    },
    {
        title: "RONDA 2 · SEMIS",
        matches: [
            { id: "s1", label: "SEMIFINAL 01", from: ["q1", "q2"] },
            { id: "s2", label: "SEMIFINAL 02", from: ["q3", "q4"] }
        ]
    },
    {
        title: "RONDA 3 · FINAL",
        matches: [{ id: "f1", label: "GRAN FINAL", from: ["s1", "s2"] }]
    }
];

const downstreamMatches = {
    q1: ["s1", "f1"],
    q2: ["s1", "f1"],
    q3: ["s2", "f1"],
    q4: ["s2", "f1"],
    s1: ["f1"],
    s2: ["f1"],
    f1: []
};

const winners = {};
const bracket = document.getElementById("bracket");
const leaderboardBody = document.getElementById("leaderboard-body");

function getMatchPlayers(match) {
    return match.players ?? match.from.map(matchId => players.find(player => player.id === winners[matchId])).filter(Boolean);
}

function renderBracket() {
    bracket.replaceChildren();

    rounds.forEach(round => {
        const roundElement = document.createElement("section");
        roundElement.className = "bracket-round";

        const heading = document.createElement("h3");
        heading.textContent = round.title;
        roundElement.append(heading);

        round.matches.forEach(match => {
            const entrants = getMatchPlayers(match);
            const card = document.createElement("article");
            card.className = `match-card${entrants.length < 2 ? " is-locked" : ""}`;

            const title = document.createElement("div");
            title.className = "match-title";
            title.innerHTML = `<span>${match.label}</span><span>${entrants.length < 2 ? "PENDIENTE" : "ELIGE GANADOR"}</span>`;
            card.append(title);

            if (entrants.length < 2) {
                const waiting = document.createElement("div");
                waiting.className = "match-empty";
                waiting.textContent = "Esperando resultados anteriores";
                card.append(waiting);
            } else {
                entrants.forEach(player => {
                    const button = document.createElement("button");
                    button.className = `match-player${winners[match.id] === player.id ? " is-winner" : ""}`;
                    button.type = "button";
                    button.dataset.match = match.id;
                    button.dataset.player = player.id;
                    button.setAttribute("aria-pressed", String(winners[match.id] === player.id));
                    button.innerHTML = `<span class="player-name">${player.name}</span><span class="player-blade">${player.blade}</span>`;
                    card.append(button);
                });
            }

            roundElement.append(card);
        });

        bracket.append(roundElement);
    });
}

function renderLeaderboard() {
    const winsByPlayer = new Map(players.map(player => [player.id, 0]));
    Object.values(winners).forEach(playerId => winsByPlayer.set(playerId, winsByPlayer.get(playerId) + 1));

    const rankedPlayers = [...players].sort((a, b) =>
        winsByPlayer.get(b.id) - winsByPlayer.get(a.id) || a.name.localeCompare(b.name, "es")
    );

    leaderboardBody.replaceChildren();
    rankedPlayers.forEach((player, index) => {
        const row = document.createElement("tr");
        row.innerHTML = `<td class="rank-cell">${String(index + 1).padStart(2, "0")}</td><td>${player.name}</td><td>${player.blade}</td><td><span class="win-count">${winsByPlayer.get(player.id)}</span></td>`;
        leaderboardBody.append(row);
    });
}

bracket.addEventListener("click", event => {
    const button = event.target.closest("button[data-match]");
    if (!button) return;

    const matchId = button.dataset.match;
    winners[matchId] = button.dataset.player;
    downstreamMatches[matchId].forEach(affectedMatch => delete winners[affectedMatch]);

    renderBracket();
    renderLeaderboard();
});

document.getElementById("reset-bracket").addEventListener("click", () => {
    Object.keys(winners).forEach(matchId => delete winners[matchId]);
    renderBracket();
    renderLeaderboard();
});

renderBracket();
renderLeaderboard();
