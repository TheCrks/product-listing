function ColorPicker() {
  return (
      <div className="color-picker">
          <div className="color-option">
              <button className="color-button" style={{ backgroundColor: '#E6CA97' }}></button>
              <button className="color-button" style={{ backgroundColor: '#D9D9D9' }}></button>
              <button className="color-button" style={{ backgroundColor: '#E1A4A9' }}></button>
          </div>
          <p className="color-label">Select Color</p>
      </div>
  );
}

export default ColorPicker;