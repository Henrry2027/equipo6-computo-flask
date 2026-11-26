// Función interactiva 1: Sugerir código de inventario según el tipo de equipo
function sugerirCodigoInventario() {
  const tipoSelect = document.getElementById("tipo_equipo");
  const codigoInput = document.getElementById("codigo_inventario");
  const mensaje = document.getElementById("mensajeJsEquipo");

  if (!tipoSelect || !codigoInput) return;

  const prefijos = {
    "Laptop": "LAP",
    "PC de Escritorio": "PC",
    "Monitor": "MON",
    "Impresora": "IMP",
    "Proyector": "PRY",
    "Switch / Red": "NET",
  };

  const prefijo = prefijos[tipoSelect.value] || "EQP";
  const aleatorio = Math.floor(100 + Math.random() * 900);
  codigoInput.value = `${prefijo}-${aleatorio}`;

  if (mensaje) {
    mensaje.textContent = `Código sugerido: ${codigoInput.value}. Puedes editarlo antes de guardar.`;
  }
}

// Función interactiva 2: Ajustar prioridad sugerida y contar caracteres en el reporte de fallas
function actualizarPrioridadYContador() {
  const categoria = document.getElementById("categoria_falla");
  const bloquea = document.getElementById("bloquea_trabajo");
  const prioridad = document.getElementById("prioridad");
  const descripcion = document.getElementById("descripcion");
  const contador = document.getElementById("contadorCaracteres");

  if (descripcion && contador) {
    const len = descripcion.value.trim().length;
    contador.textContent = `${len} / 10 caracteres mínimos recomendados`;
  }

  if (!categoria || !bloquea || !prioridad) return;

  if (bloquea.value === "si" && ["No enciende", "Energía / Batería", "Red / Internet"].includes(categoria.value)) {
    prioridad.value = "Crítica";
  } else if (bloquea.value === "si") {
    prioridad.value = "Alta";
  } else if (categoria.value === "Teclado / Mouse / Puertos") {
    prioridad.value = "Baja";
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const btnGenerar = document.getElementById("btnGenerarCodigo");
  if (btnGenerar) {
    btnGenerar.addEventListener("click", sugerirCodigoInventario);
  }

  ["categoria_falla", "bloquea_trabajo", "descripcion"].forEach((id) => {
    const el = document.getElementById(id);
    if (el) {
      el.addEventListener("input", actualizarPrioridadYContador);
      el.addEventListener("change", actualizarPrioridadYContador);
    }
  });

  actualizarPrioridadYContador();
});