import './ColorPicker.css';

function ColorPicker({ onColorSelect, selectedColor }) {
    const colorOptions = [
        { name: 'Yellow Gold', code: '#E6CA97', key: 'yellow' },
        { name: 'White Gold', code: '#D9D9D9', key: 'white' },
        { name: 'Rose Gold', code: '#E1A4A9', key: 'rose' },
    ];

    const selectedLabel = colorOptions.find(opt => opt.key === selectedColor)?.name || '';

    return (
        <div className="color-picker">
            <div className="color-options">
                {colorOptions.map(({ name, code, key }) => (
                    <div
                        key={key}
                        className={`color-button-wrapper ${selectedColor === key ? 'selected' : ''}`}
                        onClick={() => onColorSelect(key)}
                        title={`${name} (${code})`}
                    >
                        <div
                            className="color-button"
                            style={{ backgroundColor: code }}
                        />
                    </div>
                ))}
            </div>
            <p className="color-label">{selectedLabel}</p>
        </div>
    );
}

export default ColorPicker;
