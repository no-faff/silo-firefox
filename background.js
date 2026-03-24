browser.contextMenus.create({
  id: "open-with-silo",
  title: "Open with Silo",
  contexts: ["link"],
});

browser.contextMenus.onClicked.addListener((info) => {
  if (info.menuItemId === "open-with-silo") {
    browser.runtime.sendNativeMessage("com.nofaff.silo", {
      url: info.linkUrl,
    });
  }
});
