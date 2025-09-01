from pathlib import Path
from typing import List, Dict, Callable
import yaml

PROBLEMS_PATH = Path(__file__).parent / "problems.yaml"

def _questions() -> List[Dict]:
    # Representación funcional: datos inmutables (listas/dicts) y composición
    base = [
        dict(title="Invertir cadena", prompt="Invierte una cadena sin usar reversed().", hints=["Slicing [::-1]"], tags=["strings"]),
        dict(title="Filtrar pares", prompt="Filtra números pares de una lista.", hints=["filter()", "lambda"], tags=["funcional", "listas"]),
        dict(title="Map a cuadrados", prompt="Eleva al cuadrado una lista de números.", hints=["map()", "lambda"], tags=["funcional"]),
        dict(title="Reduce suma", prompt="Suma una lista usando functools.reduce.", hints=["reduce"], tags=["funcional"]),
        dict(title="Contar vocales", prompt="Cuenta el número de vocales en un texto.", hints=["in", "lower"], tags=["strings"]),
        dict(title="Flatten", prompt="Aplana una lista de listas.", hints=["sum(..., [])", "itertools.chain"], tags=["listas"]),
        dict(title="Únicos", prompt="Elimina duplicados preservando orden.", hints=["dict.fromkeys"], tags=["listas"]),
        dict(title="Componer funciones", prompt="Compón dos funciones f y g y aplícalas a una lista.", hints=["higher-order"], tags=["funcional"]),
        dict(title="Validar email", prompt="Valida un email simple por regex.", hints=["re"], tags=["regex"]),
        dict(title="Promedio por grupo", prompt="Dada una lista de (grupo, valor) calcula promedio por grupo.", hints=["groupby"], tags=["itertools"],
        ),
    ]
    return base

def _load(path: Path) -> List[Dict]:
    if path.exists():
        with path.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or []
        assert isinstance(data, list)
        return data
    return []

def _save(path: Path, data: List[Dict]) -> None:
    with path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False)

def _append(existing: List[Dict], nuevos: List[Dict]) -> List[Dict]:
    return existing + nuevos

def cargar_preguntas_funcional():
    existentes = _load(PROBLEMS_PATH)
    nuevos = _questions()
    resultado = _append(existentes, nuevos)
    _save(PROBLEMS_PATH, resultado)