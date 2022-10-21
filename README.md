# Path Finder

## Dependências

Alguns pacotes de python precisam estar instalados:

```console
pip3 install Pillow numpy tqdm
```

## Como executar:

```console
python3 pathfinder.py filepath method x_start y_start x_end y_end
```

Exemplo:

```console
python3 pathfinder.py mapas/mapa_test.map Astar 1 1 3 1
```

Os métodos aceitos são `Astar`, `BFS`, `Greedy`, `IDS` e `UCS`.
