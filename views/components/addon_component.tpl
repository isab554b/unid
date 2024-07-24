<!-- prettier-ignore -->
% for addon_key, addon in services_and_prices_content['addon_section']['addons']['addon_default'].items():
<div class="w-2/3 md:w-1/2 lg:w-2/3 mx-auto overflow-auto">
  <table class="table-auto w-full text-left whitespace-no-wrap">
    <tbody>
      <tr>
        <td class="text-unidPurple space-y-1 p-6 px-4 py-3">
          <h5>{{ addon["info"]["title"] }}</h5>
        </td>
        <td class="text-unidPurple px-4 py-3">
          <p>{{ addon["info"]["text"] }}</p>
        </td>
        <td class="px-4 py-3">
          <div class="flex items-center gap-2">
            <p
              class="text-unidPurple text-right text-xl xl:text-2xl font-saira font-bold"
            >
              {{ addon["info"]["price"] }}
            </p>
            <div class="flex flex-col text-xs text-unidPurple">
              <p>ekskl.</p>
              <p>moms</p>
            </div>
          </div>
        </td>
      </tr>
    </tbody>
    <div class="border-b border-unidLightBlue"></div>
  </table>
</div>
% end
